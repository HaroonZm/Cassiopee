while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    if max(s) < 2:
        print('NA')
    else:
        t = s.count(0)
        print(n - t + 1)