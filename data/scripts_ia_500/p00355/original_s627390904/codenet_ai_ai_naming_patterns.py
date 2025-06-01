def main():
    from sys import stdin as input_stream
    start_interval, end_interval = map(int, input_stream.readline().split())
    number_of_intervals = int(input_stream.readline())
    for interval_index in range(number_of_intervals):
        interval_start, interval_end = map(int, input_stream.readline().split())
        if end_interval <= interval_start or interval_end <= start_interval:
            continue
        else:
            print(1)
            break
    else:
        print(0)

main()