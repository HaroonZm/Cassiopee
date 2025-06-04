def process_string():
    input_string = input()
    input_length = len(input_string)
    for segment_offset in range(1, input_length // 2):
        segment_length = input_length - 2 * segment_offset
        left_half = input_string[:segment_length // 2]
        right_half = input_string[segment_length // 2:segment_length]
        if left_half == right_half:
            print(segment_length)
            break

if __name__ == "__main__":
    process_string()