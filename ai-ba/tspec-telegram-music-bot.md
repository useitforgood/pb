## System Purpose

The system is a Telegram bot that accepts artist name queries from a user and delivers audio files of selected tracks. When the user sends a message containing the phrase "top 10" along with an artist name, the system fetches the artist's top 10 tracks from the Spotify API, downloads each track via yt-dlp from YouTube, and sends the audio files to the user in the Telegram chat. When the user sends only an artist name without the phrase "top 10", the system retrieves the artist's complete discography track list from the Spotify API, presents it as a paginated inline keyboard, and downloads and sends only the tracks the user explicitly selects.

---

## Input Specification

| **Field** | **Type** | **Required** | **Source** | **Validation Rules** |
|-----------|----------|--------------|------------|----------------------|
| telegram_message_text | string | yes | user-provided | Non-empty; length ≤ 4096 characters |
| artist_query | string | yes | computed | Extracted from telegram_message_text after stripping "top 10" keyword; non-empty after trim |
| mode | enum("top10", "browse") | yes | computed | Derived from presence of "top 10" in telegram_message_text |
| callback_data | string | conditional | user-provided | Present only for inline keyboard interactions; format: "select:[track_id]", "deselect:[track_id]", "confirm", "page:[n]", "cancel" |
| TELEGRAM_BOT_TOKEN | string | yes | environment variable | Non-empty; matches Telegram token format |
| SPOTIFY_CLIENT_ID | string | yes | environment variable | Non-empty |
| SPOTIFY_CLIENT_SECRET | string | yes | environment variable | Non-empty |
| DOWNLOAD_DIR | string | yes | environment variable | Valid filesystem path; writable |

---

## Session State

| **Variable** | **Type** | **Initial value** | **Updated when** | **Scope** |
|--------------|----------|-------------------|------------------|-----------|
| artist_id | string | null | Artist search succeeds | Per user, per browse session |
| artist_name | string | null | Artist search succeeds | Per user, per browse session |
| track_list | list[Track] | [] | Album tracks aggregation completes | Per user, per browse session |
| selected_track_ids | set[string] | {} | User selects or deselects a track | Per user, per browse session |
| page | integer | 0 | User navigates pages | Per user, per browse session |
| spotify_access_token | string | null | Spotify auth succeeds | Global (shared across all users) |
| spotify_token_expiry | datetime | null | Spotify auth succeeds | Global (shared across all users) |

Session state is stored in memory keyed by `chat_id`. Session is cleared after the Download Selected Flow completes or the user cancels.

---

## Trigger and Command List

| **Trigger or Command** | **Input parameters** | **System action** | **Response** |
|------------------------|----------------------|-------------------|--------------|
| Text message containing "top 10" | Artist name embedded in message | Fetch top 10 tracks; download all; send audio files | Progress messages + audio files |
| Text message without "top 10" | Artist name | Search artist; fetch all tracks; display paginated inline keyboard | Inline keyboard with track list |
| Callback "select:[track_id]" | track_id | Add track to selected set; re-render keyboard | Updated inline keyboard |
| Callback "deselect:[track_id]" | track_id | Remove track from selected set; re-render keyboard | Updated inline keyboard |
| Callback "page:[n]" | Page number n | Update session.page; re-render keyboard | Updated inline keyboard |
| Callback "confirm" | none | Download all selected tracks; send audio files | Progress messages + audio files |
| Callback "cancel" | none | Clear session state | "Cancelled." text message |
| /start | none | Send welcome message | "Send an artist name to browse their tracks, or 'top 10 [artist]' to download their top 10 tracks." |

---

## Processing Logic

**On startup:**

1. Read `TELEGRAM_BOT_TOKEN`, `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `DOWNLOAD_DIR` from environment variables.
2. IF any required variable is missing or empty: log error to stderr; terminate process with exit code 1.
   ELSE: continue to step 3.
3. Create `DOWNLOAD_DIR` if it does not exist. IF creation fails: log error to stderr; terminate with exit code 1.
   ELSE: continue.
4. Start Telegram bot polling loop.

**On text message received:**

5. Extract `telegram_message_text` from the incoming Telegram update.
6. Normalize `telegram_message_text` to lowercase for keyword detection.
7. IF normalized text matches regex `top\s*10`: set `mode` = "top10"; extract `artist_query` by removing the matched substring and trimming whitespace.
   ELSE: set `mode` = "browse"; set `artist_query` = trimmed original `telegram_message_text`.
8. IF `artist_query` is empty after extraction: send error message "Please provide an artist name." to the user; stop processing.
   ELSE: continue to step 9.
9. IF `spotify_access_token` is null or current time ≥ `spotify_token_expiry`: call Spotify token endpoint; store `access_token` and compute `spotify_token_expiry` = current time + `expires_in` seconds.
   ELSE: continue to step 10.
10. Call Spotify Artist Search endpoint with `artist_query`. Retrieve `artist_id` and `artist_name` from top-ranked result.
11. IF no artist is returned (empty items array): send error message "Artist not found. Please check the spelling and try again." to the user; stop processing.
    ELSE: continue to step 12.
12. IF `mode` = "top10": execute the Top-10 Download Flow (steps 13–18).
    ELSE: execute the Browse Flow (steps 19–25).

**Top-10 Download Flow:**

13. Call Spotify Artist Top Tracks endpoint with `artist_id` and `market` = "US". Retrieve list of up to 10 tracks, each with `track_id`, `track_name`.
14. Send message to user: "Downloading top 10 tracks for [artist_name]…"
15. Set `success_count` = 0; set `total` = count of tracks returned.
16. FOR each track in the list (sequential, one at a time):
    a. Construct `search_query` = "[track_name] [artist_name] official audio".
    b. Invoke yt-dlp subprocess with `search_query`; output file written to `DOWNLOAD_DIR`; timeout = 30 seconds.
    c. IF yt-dlp exits with code 0 and output file exists: call Telegram sendAudio with the file; increment `success_count`; delete local file.
       ELSE: send message "Failed to download [track_name]. Skipping." to the user.
17. Send message "Done. [success_count] of [total] tracks sent."

**Browse Flow:**

18. Call Spotify Artist Albums endpoint for `artist_id` with `include_groups` = "album,single,compilation". Paginate until all albums are retrieved. Collect list of `album_id` and `release_date` values.
19. FOR each `album_id` (sequential): call Spotify Album Tracks endpoint. Paginate until all tracks are retrieved. Collect `track_id`, `track_name`, `track_number`; associate each with the album's `release_date`.
20. Aggregate all tracks. Deduplicate by normalized lowercase `track_name`: retain the first occurrence when sorted by `release_date` descending. Sort the result by `release_date` descending, then `track_number` ascending. Store as `session.track_list`.
21. Set `session.artist_id` = `artist_id`; `session.artist_name` = `artist_name`; `session.selected_track_ids` = empty set; `session.page` = 0.
22. Compute `total_pages` = ceil(count(`session.track_list`) / 20).
23. Render page 0 as an inline keyboard (see Inline Keyboard Rendering steps 29–33). Send to user with caption "Select tracks to download from [artist_name]. Page 1 of [total_pages].".

**On callback query received:**

24. Answer the callback query immediately to dismiss the loading spinner.
25. Parse `callback_data`.
26. IF `callback_data` starts with "select:": extract `track_id`; add `track_id` to `session.selected_track_ids`; re-render current page.
    ELSE IF `callback_data` starts with "deselect:": extract `track_id`; remove `track_id` from `session.selected_track_ids`; re-render current page.
    ELSE IF `callback_data` starts with "page:": extract integer `n`; set `session.page` = n; re-render page n.
    ELSE IF `callback_data` = "confirm": execute Download Selected Flow (steps 34–39).
    ELSE IF `callback_data` = "cancel": send message "Cancelled." to the user; clear session state for this `chat_id`; stop processing.
    ELSE: send inline alert "Unknown action." to the user; stop processing.

**Inline Keyboard Rendering:**

27. Compute slice: tracks at indices from (`session.page` × 20) to min((`session.page` × 20) + 20, count(`session.track_list`)) exclusive.
28. FOR each track in the slice:
    IF `track_id` is in `session.selected_track_ids`: render button label "[✓] [track_name]"; callback_data = "deselect:[track_id]".
    ELSE: render button label "[  ] [track_name]"; callback_data = "select:[track_id]".
    Each button occupies one row.
29. Append navigation row:
    IF `session.page` > 0: include button "← Prev" with callback_data = "page:[session.page - 1]".
    IF `session.page` < `total_pages` - 1: include button "Next →" with callback_data = "page:[session.page + 1]".
    IF neither condition is true: omit navigation row.
30. Append action row: button "✓ Download selected ([n])" with callback_data = "confirm" where n = count(`session.selected_track_ids`); button "✗ Cancel" with callback_data = "cancel".
31. Edit the existing inline keyboard message with the updated keyboard markup and updated caption "Select tracks to download from [artist_name]. Page [session.page + 1] of [total_pages]. Selected: [n].".

**Download Selected Flow:**

32. IF `session.selected_track_ids` is empty: send inline alert "No tracks selected." to the user; stop processing.
    ELSE: continue.
33. Edit the inline keyboard message text to "Downloading [n] selected tracks…"; remove inline keyboard.
34. Set `success_count` = 0; set `total_selected` = count(`session.selected_track_ids`).
35. FOR each `track_id` in `session.selected_track_ids` (sequential, one at a time):
    a. Retrieve `track_name` from `session.track_list` where `track_id` matches.
    b. Construct `search_query` = "[track_name] [session.artist_name] official audio".
    c. Invoke yt-dlp subprocess with `search_query`; output file written to `DOWNLOAD_DIR`; timeout = 30 seconds.
    d. IF yt-dlp exits with code 0 and output file exists: call Telegram sendAudio with the file; increment `success_count`; delete local file.
       ELSE: send message "Failed to download [track_name]. Skipping." to the user.
36. Send message "Done. [success_count] of [total_selected] tracks sent."
37. Clear session state for this `chat_id`.

---

## Data Processing

### Artist Name Extraction

Input data: raw `telegram_message_text` string.
Transformation rule: normalize to lowercase; apply regex `top\s*10`; if matched, remove the matched substring from the original string and trim whitespace to produce `artist_query`, set `mode` = "top10"; if not matched, trim the original string to produce `artist_query`, set `mode` = "browse".
Output data: `artist_query` string; `mode` enum value.

### Track Deduplication

Input data: aggregated list of tracks from all albums, each associated with an album `release_date`; may contain duplicate track names across re-releases.
Transformation rule: normalize each `track_name` to lowercase and strip whitespace; sort the full list by `release_date` descending, then `track_number` ascending; iterate in order and retain only the first occurrence of each unique normalized name; discard all subsequent duplicates.
Output data: deduplicated `session.track_list` ordered by `release_date` descending, then `track_number` ascending.

### Audio Search Query Construction

Input data: `track_name` string, `artist_name` string.
Transformation rule: concatenate as "[track_name] [artist_name] official audio" with single spaces between tokens.
Output data: `search_query` string passed as yt-dlp positional argument.

---

## External Integrations

### Spotify Web API — Client Credentials Authentication

Endpoint: `POST https://accounts.spotify.com/api/token`

| **Field** | **Location** | **Type** | **Required** | **Value** |
|-----------|-------------|----------|--------------|-----------|
| grant_type | body (form) | string | yes | "client_credentials" |
| client_id | body (form) | string | yes | SPOTIFY_CLIENT_ID |
| client_secret | body (form) | string | yes | SPOTIFY_CLIENT_SECRET |

| **Response field** | **Type** | **Used for** |
|--------------------|----------|--------------|
| access_token | string | spotify_access_token |
| expires_in | integer | computing spotify_token_expiry |

| **Code** | **Meaning** | **System action** |
|----------|-------------|-------------------|
| 400 | Invalid credentials | Log to stderr; terminate process with exit code 1 |
| 5xx | Server error | Retry 3 times with backoff (1s, 2s, 4s); if all fail, terminate |

---

### Spotify Web API — Artist Search

Endpoint: `GET https://api.spotify.com/v1/search`

| **Field** | **Location** | **Type** | **Required** | **Value** |
|-----------|-------------|----------|--------------|-----------|
| q | query | string | yes | artist_query |
| type | query | string | yes | "artist" |
| limit | query | integer | yes | 1 |
| Authorization | header | string | yes | "Bearer [spotify_access_token]" |

| **Response field** | **Type** | **Used for** |
|--------------------|----------|--------------|
| artists.items[0].id | string | artist_id |
| artists.items[0].name | string | artist_name |

| **Code** | **Meaning** | **System action** |
|----------|-------------|-------------------|
| 401 | Token expired | Re-authenticate once; retry request once; if both fail, send error to user |
| 429 | Rate limited | Wait `Retry-After` header seconds; retry up to 3 times; if all fail, send error to user |
| 4xx (other) | Client error | Send error message to user; stop processing |
| 5xx | Server error | Retry 3 times with backoff (1s, 2s, 4s); if all fail, send error to user |

---

### Spotify Web API — Artist Top Tracks

Endpoint: `GET https://api.spotify.com/v1/artists/{artist_id}/top-tracks`

| **Field** | **Location** | **Type** | **Required** | **Value** |
|-----------|-------------|----------|--------------|-----------|
| market | query | string | yes | "US" |
| Authorization | header | string | yes | "Bearer [spotify_access_token]" |

| **Response field** | **Type** | **Used for** |
|--------------------|----------|--------------|
| tracks[].id | string | track_id |
| tracks[].name | string | track_name |

Authentication: Bearer token. Error codes handled: same as Artist Search.

---

### Spotify Web API — Artist Albums

Endpoint: `GET https://api.spotify.com/v1/artists/{artist_id}/albums`

| **Field** | **Location** | **Type** | **Required** | **Value** |
|-----------|-------------|----------|--------------|-----------|
| include_groups | query | string | yes | "album,single,compilation" |
| limit | query | integer | yes | 50 |
| offset | query | integer | yes | 0, incremented by 50 per page |
| Authorization | header | string | yes | "Bearer [spotify_access_token]" |

Pagination: fetch sequentially; increment `offset` by 50 after each response until `next` field is null.

| **Response field** | **Type** | **Used for** |
|--------------------|----------|--------------|
| items[].id | string | album_id |
| items[].release_date | string | sort key |
| next | string or null | pagination termination signal |

Authentication: Bearer token. Error codes handled: same as Artist Search.

---

### Spotify Web API — Album Tracks

Endpoint: `GET https://api.spotify.com/v1/albums/{album_id}/tracks`

| **Field** | **Location** | **Type** | **Required** | **Value** |
|-----------|-------------|----------|--------------|-----------|
| limit | query | integer | yes | 50 |
| offset | query | integer | yes | 0, incremented by 50 per page |
| Authorization | header | string | yes | "Bearer [spotify_access_token]" |

Pagination: fetch sequentially until `next` field is null.

| **Response field** | **Type** | **Used for** |
|--------------------|----------|--------------|
| items[].id | string | track_id |
| items[].name | string | track_name |
| items[].track_number | integer | ordering within album |
| next | string or null | pagination termination signal |

Authentication: Bearer token. Error codes handled: same as Artist Search.

---

### yt-dlp (local subprocess)

Invocation: subprocess call to `yt-dlp` binary on system PATH.

Arguments:
- `--default-search ytsearch1`
- `--extract-audio`
- `--audio-format mp3`
- `--audio-quality 0` (320 kbps VBR)
- `--output "[DOWNLOAD_DIR]/%(title)s.%(ext)s"`
- `--no-playlist`
- `--no-warnings`
- `search_query` as the positional argument

Timeout: 30 seconds per subprocess invocation.

| **Condition** | **System action** |
|---------------|-------------------|
| Exit code ≠ 0 | Mark track as failed; notify user; continue to next track |
| Exit code = 0 but output file not found | Mark track as failed; notify user; continue |
| Subprocess exceeds 30-second timeout | Terminate subprocess; mark track as failed; notify user; continue |

No authentication required.

---

### Telegram Bot API — sendAudio

Endpoint: `POST https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendAudio`

| **Field** | **Location** | **Type** | **Required** | **Value** |
|-----------|-------------|----------|--------------|-----------|
| chat_id | body | string | yes | Incoming update's chat_id |
| audio | body | file | yes | Multipart upload of downloaded MP3 |
| title | body | string | yes | track_name |
| performer | body | string | yes | artist_name |

| **Response field** | **Type** | **Used for** |
|--------------------|----------|--------------|
| ok | boolean | Success detection |
| result.message_id | integer | Confirmation logging |

| **Code** | **Meaning** | **System action** |
|----------|-------------|-------------------|
| 400 | File rejected | Skip track; delete local file; notify user; continue |
| 429 | Rate limited | Wait `parameters.retry_after` seconds; retry up to 3 times; if all fail, skip and notify |
| 5xx | Server error | Retry 3 times with backoff (1s, 2s, 4s); if all fail, skip and notify |

---

## Output Specification

| **Field** | **Type** | **Always present** | **Description** |
|-----------|----------|--------------------|-----------------|
| audio_file | MP3 file | no | Downloaded audio track delivered via Telegram sendAudio |
| status_message | string | yes | Text message sent to user indicating progress, completion, or error |
| inline_keyboard | InlineKeyboardMarkup | no | Paginated track list with selection state; present only in Browse Flow |

Delivery method: all outputs sent via Telegram Bot API to the user's `chat_id`. Local MP3 files are deleted from `DOWNLOAD_DIR` immediately after successful or failed transmission.

---

## Error Handling

| **Error condition** | **Source** | **System behavior** | **Response to user** |
|--------------------|------------|--------------------|-----------------------|
| Empty artist name after extraction | Input parsing | Stop processing | "Please provide an artist name." |
| Spotify artist search returns zero results | Spotify API | Stop processing | "Artist not found. Please check the spelling and try again." |
| Spotify API returns 401 | Spotify API | Re-authenticate once; retry; if both fail, stop | "Service authentication error. Please try again later." |
| Spotify API returns 429, all retries exhausted | Spotify API | Stop processing | "Service is busy. Please try again later." |
| Spotify API returns 5xx, all retries exhausted | Spotify API | Stop processing | "Service temporarily unavailable. Please try again later." |
| yt-dlp exits with non-zero code | yt-dlp | Skip track; continue | "Failed to download [track_name]. Skipping." |
| yt-dlp subprocess exceeds 30-second timeout | yt-dlp | Terminate subprocess; skip track; continue | "Failed to download [track_name] (timeout). Skipping." |
| Output file not found after yt-dlp exit code 0 | yt-dlp | Skip track; continue | "Failed to download [track_name]. Skipping." |
| Telegram sendAudio returns 400 | Telegram API | Skip track; delete local file; continue | "Could not send [track_name] (file rejected)." |
| Telegram sendAudio returns 429, all retries exhausted | Telegram API | Skip track; delete local file; continue | "Could not send [track_name]. Skipping." |
| Confirm callback with no tracks selected | User action | Stop processing | Inline alert: "No tracks selected." |
| Unrecognized callback_data value | Callback | Log warning; stop processing | Inline alert: "Unknown action." |
| TELEGRAM_BOT_TOKEN missing at startup | Startup | Terminate (exit code 1) | stderr: "TELEGRAM_BOT_TOKEN environment variable not set." |
| SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET missing at startup | Startup | Terminate (exit code 1) | stderr: "Spotify credentials not set." |
| DOWNLOAD_DIR not writable at startup | Startup | Terminate (exit code 1) | stderr: "DOWNLOAD_DIR is not writable." |

---

## Completion Criteria

1. When the user sends a message containing "top 10" and a valid artist name, the system sends up to 10 audio files followed by a summary message stating how many tracks were successfully delivered.
2. When the user sends only an artist name (without "top 10") and the artist exists on Spotify, the system replies with a paginated inline keyboard displaying the artist's full deduplicated track list at 20 tracks per page.
3. When the user navigates pages, the inline keyboard message is edited in place to show the correct page slice without sending a new message.
4. When the user selects a track, the corresponding button label changes to include a checkmark; when the user deselects it, the checkmark is removed.
5. When the user presses "✓ Download selected" with at least one track selected, the system downloads and delivers exactly the selected tracks as audio files, followed by a summary message.
6. When the user presses "✗ Cancel", session state is cleared, no downloads are initiated, and the user receives a "Cancelled." message.
7. When the artist is not found on Spotify, the system sends an error message and performs no download.
8. When a track download fails for any reason, the system skips that track, notifies the user with the track name, and continues processing the remaining tracks.
9. When a required environment variable is absent at startup, the process terminates immediately with a descriptive message logged to stderr and exit code 1.
10. All downloaded MP3 files are deleted from `DOWNLOAD_DIR` immediately after each transmission attempt, whether successful or not.

---

## Deployment Instructions

### Prerequisites

- Python 3.11 or later
- `pip` package manager
- `ffmpeg` binary on system PATH (required by yt-dlp for audio conversion)
- A Telegram bot token — create a bot via @BotFather on Telegram using the `/newbot` command
- A Spotify Developer application — register at the Spotify Developer Dashboard; note the Client ID and Client Secret from the application settings page

### Python dependencies (requirements.txt)

```
python-telegram-bot==21.6
spotipy==2.24.0
yt-dlp==2024.11.18
python-dotenv==1.0.1
```

### Environment variables (.env)

```
TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
SPOTIFY_CLIENT_ID=<your_spotify_client_id>
SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>
DOWNLOAD_DIR=/tmp/music_bot_downloads
```

### Local installation

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Install ffmpeg
# macOS:
brew install ffmpeg
# Ubuntu/Debian:
sudo apt-get update && sudo apt-get install -y ffmpeg

# Create the .env file with all four required variables (see above)

# Run the bot
python bot.py
```

### Docker deployment

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .

ENV DOWNLOAD_DIR=/tmp/downloads

CMD ["python", "bot.py"]
```

**Build and run:**

```bash
docker build -t telegram-music-bot .

docker run -d \
  --name music-bot \
  --restart unless-stopped \
  -e TELEGRAM_BOT_TOKEN=your_token \
  -e SPOTIFY_CLIENT_ID=your_client_id \
  -e SPOTIFY_CLIENT_SECRET=your_client_secret \
  -e DOWNLOAD_DIR=/tmp/downloads \
  telegram-music-bot
```

**View logs:**

```bash
docker logs -f music-bot
```

### systemd service (Linux VPS)

Create `/etc/systemd/system/music-bot.service`:

```ini
[Unit]
Description=Telegram Music Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/music-bot
EnvironmentFile=/home/ubuntu/music-bot/.env
ExecStart=/home/ubuntu/music-bot/venv/bin/python bot.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable music-bot
sudo systemctl start music-bot
sudo systemctl status music-bot
```

**View logs:**

```bash
journalctl -u music-bot -f
```

### Verification checklist after deployment

- [ ] Bot responds to `/start` with the welcome message
- [ ] Sending "top 10 The Beatles" triggers a download sequence and delivers audio files
- [ ] Sending "The Beatles" returns a paginated inline keyboard
- [ ] Selecting tracks and pressing "✓ Download selected" delivers only those tracks
- [ ] Pressing "✗ Cancel" clears the session and sends "Cancelled."
- [ ] An unknown artist name returns the "Artist not found." error message
- [ ] No MP3 files remain in `DOWNLOAD_DIR` after each download sequence completes
