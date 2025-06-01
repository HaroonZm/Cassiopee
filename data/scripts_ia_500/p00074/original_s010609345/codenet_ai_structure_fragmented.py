#!/usr/bin/python

def read_input():
    return map(int, raw_input().split())

def is_termination(h, m, s):
    return h == -1 and m == -1 and s == -1

def total_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def get_full_duration():
    return 2 * 3600

def calculate_remaining(full, elapsed):
    return full - elapsed

def convert_seconds_to_hms(seconds):
    h = int(seconds / 3600)
    remainder = seconds - h * 3600
    m = int(remainder / 60)
    s = remainder - m * 60
    return h, m, s

def convert_remaining_to_hms(rest):
    return convert_seconds_to_hms(rest)

def convert_remaining_to_thms(rest):
    th = int(rest / 1200)
    remainder = rest - th * 1200
    tm = int(remainder / 20)
    ts = (remainder - tm * 20) * 3
    return th, tm, ts

def format_time(h, m, s):
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

def process_time_inputs():
    while True:
        h, m, s = read_input()
        if is_termination(h, m, s):
            break

        full = get_full_duration()
        elapsed = total_seconds(h, m, s)
        rest = calculate_remaining(full, elapsed)
        
        h1, m1, s1 = convert_remaining_to_hms(rest)
        h2, m2, s2 = convert_remaining_to_thms(rest)

        print format_time(h1, m1, s1)
        print format_time(h2, m2, s2)

process_time_inputs()