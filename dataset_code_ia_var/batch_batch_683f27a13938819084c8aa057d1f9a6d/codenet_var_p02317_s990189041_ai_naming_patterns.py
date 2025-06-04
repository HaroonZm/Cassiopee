import bisect

input_count = int(input())
input_sequence = [int(input()) for input_index in range(input_count)]

subsequence_ends = [input_sequence[0]]

for sequence_index in range(1, input_count):
    if subsequence_ends[-1] < input_sequence[sequence_index]:
        subsequence_ends.append(input_sequence[sequence_index])
    else:
        replace_index = bisect.bisect_left(subsequence_ends, input_sequence[sequence_index])
        subsequence_ends[replace_index] = input_sequence[sequence_index]

print(len(subsequence_ends))