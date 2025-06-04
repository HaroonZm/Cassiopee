from collections import defaultdict
while True:
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0:
        break
    dic = defaultdict(int)
    i = 0
    while i < n:
        d_v = input().split()
        d = int(d_v[0])
        v = int(d_v[1])
        if dic[d] < v:
            dic[d] = v
        i += 1
    total = 0
    for val in dic.values():
        total += val
    print(total)