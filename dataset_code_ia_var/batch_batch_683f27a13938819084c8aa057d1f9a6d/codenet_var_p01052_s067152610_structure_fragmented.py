def read_n():
    return int(input())

def read_movie():
    a, b = map(int, input().split())
    return a, b

def build_table(n):
    tbl = []
    for i in range(n):
        a, b = read_movie()
        tbl.append([b, a])
    return tbl

def sort_table(tbl):
    tbl.sort()
    return tbl

def init_seen(n):
    return [0]*101

def check_available(day, movie):
    return movie[1] <= day <= movie[0]

def check_seen(j, seen):
    return seen[j]

def mark_seen(j, seen):
    seen[j] = 1

def add_points(ans):
    return ans + 100

def add_saw(saw):
    return saw + 1

def process_day(i, n, tbl, seen, ans, saw):
    for j in range(n):
        if not check_available(i, tbl[j]):
            continue
        if check_seen(j, seen):
            continue
        ans = add_points(ans)
        mark_seen(j, seen)
        saw = add_saw(saw)
        break
    return ans, saw

def calc_missing_points(saw):
    return (31 - saw) * 50

def main():
    n = read_n()
    tbl = build_table(n)
    tbl = sort_table(tbl)
    ans = 0
    saw = 0
    seen = init_seen(n)
    for i in range(1, 32):
        ans, saw = process_day(i, n, tbl, seen, ans, saw)
    print(ans + calc_missing_points(saw))

main()