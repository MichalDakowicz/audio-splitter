# Audio Splitter

This Python script offers a flexible way to split audio files (MP3 format) into smaller segments based on timestamps provided either directly on the command line or within a text file.

## **Features**

-   Accepts timestamps in either HH:MM:SS or seconds format.
-   Leverages ffmpeg for audio processing.
-   Generates output files with a numbered prefix for easy organization.
-   Supports reading timestamps from a file for more convenient handling of larger lists.

## **Prerequisites**

-   Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
-   ffmpeg installed on your system ([https://ffmpeg.org/download.html](https://ffmpeg.org/download.html))

## **Installation**

1. Download or copy the Python script (`audio_splitter.py`).
2. Ensure you have ffmpeg installed. If needed, you can find installation tutorials online (The one i would recommend would be: [https://www.youtube.com/watch?v=r1AtmY-RMyQ](https://www.youtube.com/watch?v=r1AtmY-RMyQ)).

## **Usage**

Run the script from your command line/terminal. There are two ways to provide timestamps:

**1. Directly on the Command Line:**

```bash
python audio_splitter.py <input_file.mp3> <output_prefix> --timestamps "<timestamp1>,<timestamp2>,..."
```

**1.1 Example (using a timestamps):**

```bash
python audio_splitter.py interview.mp3 interview_part --timestamps "00:19:25,00:21:30,00:21:30,00:25:12,00:25:12,00:28:45"
```

**2. Using a Timestamps File:**

a. Create a plain text file (e.g., `timestamps.txt`) with one timestamp pair per line:

      00:19:25,00:21:30
      00:21:30,00:25:12
      ... and so on

b. Run the script, specifying your timestamps file:

```bash
python audio_splitter.py <input_file.mp3> <output_prefix> --timestamps timestamps.txt
```

**2.1 Example (using a timestamps file):**

```bash
python audio_splitter.py interview.mp3 interview_part --timestamps timestamps.txt
```

## **Explanation of Arguments**

-   `<input_file.mp3>`: The path to the MP3 file you wish to split.
-   `<output_prefix>`: The desired prefix for the generated output files (e.g., 'interview_part').
-   `--timestamps`:
    -   If providing timestamps directly, use a comma-separated list within quotes (e.g., `"00:01:23,00:05:00,12.5,20.0"`).
    -   If using a file, provide the path to your timestamps file (e.g., `timestamps.txt`).

## **Output**

The script will create multiple MP3 files in the same directory, named with your specified output prefix and numbered sequentially (e.g., interview_part_1.mp3, interview_part_2.mp3).

## **Notes**

-   Ensure you have the necessary permissions to write files in the output directory.
-   For very large lists of timestamps, it might be more efficient to split your timestamps into multiple files and run the script multiple times.
