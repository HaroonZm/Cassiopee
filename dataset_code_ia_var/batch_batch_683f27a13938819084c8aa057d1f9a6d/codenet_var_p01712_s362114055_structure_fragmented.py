def read():
    return list(map(int, input().split()))

def read_test_case():
    n, w, h = read()
    bases = []
    for _ in range(n):
        bases.append(read())
    return n, w, h, bases

def compute_intervals_x(bases, w):
    return [(x - w, x + w) for x, y, w in bases]

def compute_intervals_y(bases, w):
    return [(y - w, y + w) for x, y, w in bases]

def sort_intervals(intervals):
    return sorted(intervals, key=lambda lr: lr[0])

def unzip_intervals(sorted_intervals):
    return zip(*sorted_intervals)

def check_cover(ls, rs, target):
    x = 0
    res = True
    for l, r in zip(ls, rs):
        if l > x:
            res = False
            break
        x = max(x, r)
    if target > x:
        res = False
    return res

def process_case(n, w, h, bases):
    intervals_x = compute_intervals_x(bases, w)
    sorted_x = sort_intervals(intervals_x)
    ls_x, rs_x = unzip_intervals(sorted_x)
    res1 = check_cover(ls_x, rs_x, w)

    intervals_y = compute_intervals_y(bases, w)
    sorted_y = sort_intervals(intervals_y)
    ls_y, rs_y = unzip_intervals(sorted_y)
    res2 = check_cover(ls_y, rs_y, h)

    return "Yes" if res1 or res2 else "No"

def main():
    while True:
        try:
            n, w, h, bases = read_test_case()
        except:
            break
        result = process_case(n, w, h, bases)
        print(result)

main()