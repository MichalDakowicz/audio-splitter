# Audio Splitting Toolkit

This toolkit provides a convenient way to split audio files, particularly those with timestamps derived from YouTube videos.

## Prerequisites

-   Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
-   ffmpeg ([https://ffmpeg.org/download.html](https://ffmpeg.org/download.html))

## Workflow

1. **Obtain Timestamps:**

    - **Direct Input:** If you already have timestamps in the correct format (HH:MM:SS or seconds), proceed to step 4.
    - **YouTube Timestamps:**
        1. Copy the timestamps from the YouTube video description.
        2. Paste them into a plain text file (e.g., `youtube_timestamps.txt`).

2. **Convert YouTube Timestamps (if needed):**

    ```bash
    python convert_yt_timestamps.py youtube_timestamps.txt converted_timestamps.txt <video_length>
    ```

    - Replace `<video_length>` with the video's total duration in HH:MM:SS format (e.g., "01:25:40").

3. **Split Your Audio File:**
    ```bash
    python audio_splitter.py <input_file.mp3> <output_prefix> --timestamps converted_timestamps.txt
    ```
    - Replace `<input_file.mp3>` with the path to your audio file.
    - Replace `<output_prefix>` with your desired naming prefix for the output segments.

## Detailed Explanation of Scripts

-   **audio_splitter.py**

    -   Takes an MP3 file and splits it into smaller segments based on provided timestamps.
    -   Supports timestamps in the following formats:
        -   HH:MM:SS (e.g., "00:12:35")
        -   Seconds (e.g., "12.5")
    -   Accepts timestamps either as a comma-separated list on the command line or from a text file.

-   **convert_yt_timestamps.py**
    -   Transforms raw timestamps copied from YouTube video descriptions into the format compatible with `audio_splitter.py`.
    -   Requires the total length of the corresponding video.

## Notes

-   Ensure you have permissions to write files in the directory where you execute the scripts.
-   For extensive lists of timestamps, consider splitting your timestamps into multiple files and running the `audio_splitter.py` script multiple times for better management.

## Example

Assuming you have a podcast named "interview.mp3" and copied YouTube timestamps into "yt_timestamps.txt":

1. **Convert Timestamps:**

    ```bash
    python convert_yt_timestamps.py yt_timestamps.txt converted_timestamps.txt 01:55:20
    ```

    (Assuming the podcast is 1 hour, 55 minutes, and 20 seconds long)

2. **Split the Audio:**
    ```bash
    python audio_splitter.py interview.mp3 interview_segment --timestamps converted_timestamps.txt
    ```

Let me know if you have any other scenarios or features you'd like to showcase!
