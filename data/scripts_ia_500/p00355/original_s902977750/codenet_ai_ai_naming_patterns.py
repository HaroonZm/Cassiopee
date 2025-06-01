def main():
    start_interval, end_interval = map(int, input().split())

    number_of_ranges = int(input())
    start_points, end_points = [], []
    for _ in range(number_of_ranges):
        start_point, end_point = map(int, input().split())
        start_points.append(start_point)
        end_points.append(end_point)

    for index in range(number_of_ranges):
        if end_points[index] <= start_interval or end_interval <= start_points[index]:
            continue
        else:
            return 1
    return 0

if __name__ == '__main__':
    print(main())