import subprocess
import argparse
import wave
import contextlib

def get_duration(filename):
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

def split_audio(input_file, output_file, start_time, end_time):
    cmd = "ffmpeg -i " + input_file + " -ss " + start_time + " -to " + end_time + " -c:a libmp3lame " + output_file
    subprocess.call(cmd, shell=True)

def main():
    parser = argparse.ArgumentParser(description='Split audio file into parts based on time stamps')
    parser.add_argument('input_file', type=str, help='Input audio file (MP3)')
    parser.add_argument('output_prefix', type=str, help='Output audio file prefix')
    parser.add_argument('--timestamps', type=str, default='timestamps.txt',
                        help='File containing timestamps in the format HH:MM:SS or seconds (e.g., 00:01:23, 12.5). Default: timestamps.txt')
    args = parser.parse_args()

    input_file = args.input_file
    output_prefix = args.output_prefix
    timestamps_file = args.timestamps

    with open(timestamps_file, 'r') as f:
        timestamps = [line.strip().split(',') for line in f.readlines()]

    for i, timestamp_pair in enumerate(timestamps):
        start_time = timestamp_pair[0]
        end_time = timestamp_pair[1]
        output_file = output_prefix + '_' + str(i + 1) + ".mp3"
        split_audio(input_file, output_file, start_time, end_time)

if __name__ == "__main__":
    main()
