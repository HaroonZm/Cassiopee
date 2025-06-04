from collections import deque
import sys

def parse_input():
    return int(input())

def process_commands(n):
    sum_d = 0
    aa = create_deque()
    for _ in range(n):
        qq = read_command()
        if is_appendleft(qq):
            append_to_left(aa, qq[1])
        elif is_rotate(qq):
            rotate_left(aa, qq[1])
            sum_d = update_sum(sum_d, qq[1])
        else:
            pop_left(aa)
    return aa, sum_d

def create_deque():
    return deque()

def read_command():
    return list(map(int, input().split()))

def is_appendleft(qq):
    return qq[0] == 0

def is_rotate(qq):
    return qq[0] == 1

def append_to_left(aa, val):
    aa.appendleft(val)

def rotate_left(aa, steps):
    aa.rotate(-steps)

def update_sum(sum_d, val):
    return sum_d + val

def pop_left(aa):
    aa.popleft()

def finalize_rotation(aa, sum_d):
    aa.rotate(sum_d)
    return aa

def print_deque(aa):
    for a in aa:
        print(a)

def main():
    n = parse_input()
    aa, sum_d = process_commands(n)
    aa = finalize_rotation(aa, sum_d)
    print_deque(aa)

main()