import sys

def calculate_total_cost(start_time, end_time, cost_before_zero, cost_at_zero, cost_after_zero):
    total_cost = 0
    current_time = start_time
    while current_time < end_time:
        if current_time < 0:
            current_time += 1
            total_cost += cost_before_zero
        elif current_time == 0:
            current_time += 1
            total_cost += (cost_at_zero + cost_after_zero)
        else:
            current_time += 1
            total_cost += cost_after_zero
    return total_cost

def main(program_arguments):
    input_start_time = int(input())
    input_end_time = int(input())
    input_cost_before_zero = int(input())
    input_cost_at_zero = int(input())
    input_cost_after_zero = int(input())
    result = calculate_total_cost(
        input_start_time,
        input_end_time,
        input_cost_before_zero,
        input_cost_at_zero,
        input_cost_after_zero
    )
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])