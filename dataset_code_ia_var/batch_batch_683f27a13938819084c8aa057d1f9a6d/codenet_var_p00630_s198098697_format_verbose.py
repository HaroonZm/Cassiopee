while True:

    input_string, conversion_code = input().split()

    if conversion_code == "X":
        break

    if "_" in input_string:
        word_segments = input_string.split("_")
    else:
        word_segments = []
        word_start_index = 0

        for current_index in range(1, len(input_string)):
            if input_string[current_index].isupper():
                word_segments.append(input_string[word_start_index:current_index])
                word_start_index = current_index

        word_segments.append(input_string[word_start_index:])

    if conversion_code == "U":

        for segment_index in range(len(word_segments)):
            word_segments[segment_index] = (
                word_segments[segment_index][0].upper() + word_segments[segment_index][1:]
            )

        print("".join(word_segments))

    elif conversion_code == "L":

        word_segments[0] = word_segments[0].lower()

        for segment_index in range(1, len(word_segments)):
            word_segments[segment_index] = (
                word_segments[segment_index][0].upper() + word_segments[segment_index][1:]
            )

        print("".join(word_segments))

    else:

        for segment_index in range(len(word_segments)):
            word_segments[segment_index] = word_segments[segment_index].lower()

        print("_".join(word_segments))