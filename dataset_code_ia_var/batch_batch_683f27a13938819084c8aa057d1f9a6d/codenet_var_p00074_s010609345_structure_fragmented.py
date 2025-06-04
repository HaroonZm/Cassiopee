def read_input():
    return raw_input().strip()

def parse_time_input(input_str):
    return list(map(int, input_str.split()))

def should_exit(time_tuple):
    return time_tuple[0] == time_tuple[1] == time_tuple[2] == -1

def seconds_from_hms(h, m, s):
    return h * 3600 + m * 60 + s

def full_cycle_seconds():
    return 2 * 3600

def remaining_seconds(full, elapsed):
    return full - elapsed

def extract_hms(rem):
    h = int(rem / 3600)
    m = int((rem - h * 3600) / 60)
    s = rem - h * 3600 - m * 60
    return (h, m, s)

def extract_thms(rest):
    th = int(rest / 1200)
    tm = int((rest - th * 1200) / 20)
    ts = (rest - th * 1200 - tm * 20) * 3
    return (th, tm, ts)

def format_time(h, m, s):
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

def print_times(t1, t2):
    print(format_time(*t1))
    print(format_time(*t2))

def main_loop():
    while True:
        inp = read_input()
        time_tuple = parse_time_input(inp)
        if should_exit(time_tuple):
            break
        elapsed = seconds_from_hms(*time_tuple)
        full = full_cycle_seconds()
        rest = remaining_seconds(full, elapsed)
        first = extract_hms(rest)
        second = extract_thms(rest)
        print_times(first, second)

if __name__ == "__main__":
    main_loop()