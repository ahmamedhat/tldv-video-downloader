# TLDV Video Downloader

A simple Python script to download videos from [tldv.io](https://tldv.io/) when you have access to the meeting.

## Prerequisites

- Python 3.6+
- `ffmpeg` installed and available in your PATH
- Required Python packages:
  - `requests`

## Installation

1. Clone or download this repository to your local machine

2. Install dependencies:

   Using pip:

   ```bash
   pip install requests
   ```

   Using uv (faster alternative to pip):

   ```bash
   # Install uv first (if not already installed)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Create a virtual environment and install dependencies
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   # or .venv\Scripts\activate  # On Windows

   uv pip install requests
   ```

3. Install ffmpeg:

   On macOS:

   ```bash
   brew install ffmpeg
   ```

   On Ubuntu/Debian:

   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

   On Windows, download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your PATH.

## Usage

1. Go to [tldv.io](https://tldv.io/) and log in
2. Navigate to the meeting you want to download
3. Copy the URL of the meeting (e.g., `https://tldv.io/app/meeting/123456abcdef`)
4. Open the browser developer tools (F12 or Right-click > Inspect)
5. Go to the Network tab
6. Refresh the page
7. Look for a request to `https://gw.tldv.io/v1/meetings/[MEETING_ID]/watch-page`
8. Find the "Authorization" header in the request headers
9. Copy the value (it starts with "Bearer ", but you only need to copy the token part after "Bearer ")

Once you have the URL and Authorization token:

1. Run the script:
   ```bash
   # If using a virtual environment, make sure it's activated
   python tldv.py
   ```
2. When prompted, paste the URL of the meeting
3. When prompted for the Auth token, paste the token you copied earlier
4. The script will download the video and save it as an MP4 file with the meeting date and name

## Troubleshooting

- **"Invalid authorization header format" error**: Make sure you're only copying the token part after "Bearer " from the Authorization header.
- **ffmpeg not found**: Ensure ffmpeg is properly installed and added to your PATH.
- **Permission denied**: Run the script with appropriate permissions to write to the current directory.

## Notes

- The script also saves a JSON file with all metadata about the meeting alongside the video file.
- The downloaded videos are named with the format: `[DATE]_[MEETING_NAME].mp4`
- All credits goes to [Akash's original code](https://gist.github.com/akash-gajjar/24fc183f6b25c74750606606f2319d01)
