from datetime import datetime as dt

def split_times(two_times):
    return two_times.split()

def extract_in_time_str(times):
    return ' '.join(times[:3])

def extract_out_time_str(times):
    return ' '.join(times[3:])

def parse_time(time_str):
    return dt.strptime(time_str, '%H %M %S')

def calculate_duration(in_time, out_time):
    return out_time - in_time

def duration_to_seconds(duration):
    return duration.seconds

def seconds_to_hms(seconds):
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    sec = seconds % 60
    return hour, minute, sec

def format_duration(hour, minute, sec):
    return '{} {} {}'.format(hour, minute, sec)

def while_in_time(two_times):
    times = split_times(two_times)
    in_time_str = extract_in_time_str(times)
    out_time_str = extract_out_time_str(times)
    in_time = parse_time(in_time_str)
    out_time = parse_time(out_time_str)
    duration = calculate_duration(in_time, out_time)
    seconds = duration_to_seconds(duration)
    hour, minute, sec = seconds_to_hms(seconds)
    str_while_time = format_duration(hour, minute, sec)
    return str_while_time

def read_input():
    return input()

def main():
    A_time = read_input()
    B_time = read_input()
    C_time = read_input()
    print(while_in_time(A_time))
    print(while_in_time(B_time))
    print(while_in_time(C_time))

main()