import sys

def compute_remaining_time(initial_time_seconds):
    number_of_tasks = int(input())
    remaining_time = initial_time_seconds
    for _ in range(number_of_tasks):
        start_time, finish_time = map(int, input().split())
        remaining_time -= (finish_time - start_time)
    if remaining_time <= 0:
        return 'OK'
    return remaining_time

def main_program(arguments_list):
    while True:
        total_time_seconds = int(input())
        if total_time_seconds == 0:
            break
        result = compute_remaining_time(total_time_seconds)
        print(result)

if __name__ == '__main__':
    main_program(sys.argv[1:])