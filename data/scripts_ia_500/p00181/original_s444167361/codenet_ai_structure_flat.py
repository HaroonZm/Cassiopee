import sys
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    books = [int(input()) for _ in range(n)]
    ub = 1500000
    lb = 0
    min_width = float('inf')
    for _ in range(100):
        mid = (ub + lb) // 2
        if max(books) > mid:
            cond = False
        else:
            rem = mid
            count = m
            i = 0
            while i < n:
                if books[i] <= rem:
                    rem -= books[i]
                    i += 1
                else:
                    rem = mid
                    count -= 1
                    if count == 0:
                        break
            cond = count > 0 or (count == 0 and i == n)
        if cond:
            min_width = min(min_width, mid)
            ub = mid
        else:
            lb = mid
    print(min_width)