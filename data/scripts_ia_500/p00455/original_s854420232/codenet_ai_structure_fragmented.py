def read_triplet():
    return list(map(int, input().split()))

def get_seconds_diff(r):
    if r[5] - r[2] >= 0:
        return r[5] - r[2]
    else:
        return 60 - (r[2] - r[5])

def adjust_minute_if_seconds_borrow(r):
    if r[5] - r[2] < 0:
        r[4] -= 1

def get_minutes_diff(r):
    if r[4] - r[1] >= 0:
        return r[4] - r[1]
    else:
        return 60 - (r[1] - r[4])

def adjust_hour_if_minutes_borrow(r):
    if r[4] - r[1] < 0:
        r[3] -= 1

def get_hours_diff(r):
    return r[3] - r[0]

def process_triplet(r):
    adjust_minute_if_seconds_borrow(r)
    s = get_seconds_diff(r)
    adjust_hour_if_minutes_borrow(r)
    m = get_minutes_diff(r)
    h = get_hours_diff(r)
    print(h, m, s)

def main():
    t = [read_triplet() for _ in range(3)]
    for r in t:
        process_triplet(r)

main()