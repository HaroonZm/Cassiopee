import sys
from sys import stdin
from math import ceil

def read_input():
    return int(stdin.readline())

def compute_required_days(homework_amount, daily_limit):
    return ceil(homework_amount / daily_limit)

def calculate_remaining_days(total_days, required_days_a, required_days_b):
    return total_days - max(required_days_a, required_days_b)

def main(args):
    total_days = read_input()
    homework_a = read_input()
    homework_b = read_input()
    limit_a = read_input()
    limit_b = read_input()
    
    days_needed_a = compute_required_days(homework_a, limit_a)
    days_needed_b = compute_required_days(homework_b, limit_b)
    
    remaining_days = calculate_remaining_days(total_days, days_needed_a, days_needed_b)
    print(remaining_days)

if __name__ == '__main__':
    main(sys.argv[1:])