while True:
    try:
        n = int(input())
    except:
        break
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    s = 0
    i = 0
    for x in a_sorted:
        s += (n - i) * x
        i += 1
    print(s)