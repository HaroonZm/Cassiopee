while True:
    remaining_count = int(input())
    if remaining_count == 0:
        break
    segment_count = int(input())
    for _ in range(segment_count):
        start_end_values = list(map(int, input().split()))
        remaining_count -= (start_end_values[1] - start_end_values[0])
    print(remaining_count if remaining_count > 0 else 'OK')