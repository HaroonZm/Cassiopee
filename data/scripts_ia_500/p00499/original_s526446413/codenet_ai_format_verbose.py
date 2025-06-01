import sys
from sys import stdin
from math import ceil

input = stdin.readline

def main(args):
    
    total_available_days = int(input())
    
    work_amount_A = int(input())
    work_amount_B = int(input())
    
    daily_work_capacity_A = int(input())
    daily_work_capacity_B = int(input())
    
    days_needed_for_A = ceil(work_amount_A / daily_work_capacity_A)
    days_needed_for_B = ceil(work_amount_B / daily_work_capacity_B)
    
    remaining_days_after_work = total_available_days - max(days_needed_for_A, days_needed_for_B)
    
    print(remaining_days_after_work)

if __name__ == '__main__':
    main(sys.argv[1:])