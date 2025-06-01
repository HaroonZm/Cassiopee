import sys
import os

while True:
    total_time_required = int(input())
    if total_time_required == 0:
        break
    number_of_shifts = int(input())
    shifts = [list(map(int, input().split())) for _ in range(number_of_shifts)]
    
    total_shift_time = 0
    for shift in shifts:
        shift_start, shift_end = shift
        if shift_start > shift_end:
            total_shift_time += shift_end - (shift_start - 24)
        else:
            total_shift_time += shift_end - shift_start
    
    if total_shift_time >= total_time_required:
        print("OK")
    else:
        print(total_time_required - total_shift_time)