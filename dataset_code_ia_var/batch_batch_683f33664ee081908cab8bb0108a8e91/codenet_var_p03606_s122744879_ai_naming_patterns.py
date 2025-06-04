segment_count = int(input())
total_length = 0
for segment_index in range(segment_count):
    segment_start, segment_end = map(int, input().split())
    segment_length = segment_end - segment_start + 1
    total_length += segment_length
print(total_length)