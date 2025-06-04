import math

def read_input():
    try:
        return float(input())
    except EOFError:
        return None

def calculate_time(initial_velocity):
    return initial_velocity / 9.8

def calculate_height(time_value):
    return 4.9 * time_value ** 2

def calculate_floor(height_value):
    return int((height_value + 5) // 5 + 1)

def main():
    while True:
        input_velocity = read_input()
        if input_velocity is None:
            break
        time_result = calculate_time(input_velocity)
        height_result = calculate_height(time_result)
        floor_number = calculate_floor(height_result)
        print(floor_number)

main()