import argparse

def convert_timestamps(input_file, output_file, time):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        lines = f_in.readlines()
        for i in range(len(lines)):
            start_time = lines[i].split(' - ')[0]
            start_time = '00:' + start_time if len(start_time) <= 5 else start_time
            start_time = ':'.join([f'{int(t):02d}' for t in start_time.split(':')])  # Pad each segment with zeros
            if i < len(lines) - 1:
                end_time = lines[i + 1].split(' - ')[0]
                end_time = '00:' + end_time if len(end_time) <= 5 else end_time
                end_time = ':'.join([f'{int(t):02d}' for t in end_time.split(':')])  # Pad each segment with zeros
            else:
                end_time = time
            f_out.write(f'{start_time},{end_time}\n')

def main():
    parser = argparse.ArgumentParser(description='Convert YouTube timestamps to the format needed by the audio splitter script')
    parser.add_argument('input_file', type=str, help='Input file with YouTube timestamps')
    parser.add_argument('output_file', type=str, help='Output file for converted timestamps')
    parser.add_argument('end_time', type=str, help='End time for the last segment')
    args = parser.parse_args()

    convert_timestamps(args.input_file, args.output_file, args.end_time)

if __name__ == "__main__":
    main()