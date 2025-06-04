from sys import stdin
from itertools import starmap

TIME_RANGES = [(660, 899), (1080, 1259), (1260, 1559)]
SLOTS = ["lunch", "dinner", "midnight"]

def parse_time(hm):
    h, m = map(int, hm.split(":"))
    return h + 24 if h <= 2 else h, m

def find_slot(mins):
    for idx, (start, end) in enumerate(TIME_RANGES):
        if start <= mins <= end:
            return idx
    return None

def process_case(case_lines):
    cnt = [0] * 3
    ok = [0] * 3
    for line in case_lines:
        time_str, MM = line.split()
        h, m = parse_time(time_str)
        MM = int(MM)
        t = h * 60 + m
        # Calculate end time in minutes
        MM = MM + h * 60 if MM >= m else MM + (h + 1) * 60
        idx = find_slot(t)
        if idx is not None:
            cnt[idx] += 1
            if MM - t <= 8:
                ok[idx] += 1
    for guests, goods, label in zip(cnt, ok, SLOTS):
        print(f"{label} ", end="")
        print("no guest" if guests == 0 else goods * 100 // guests)

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n = int(next(lines))
        except StopIteration:
            break
        if n == 0:
            break
        process_case([next(lines) for _ in range(n)])

if __name__ == "__main__":
    main()