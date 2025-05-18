from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())
c_lst = list(map(int, input().split()))
for t in cwr((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), n):
    out = ""
    cost = 0
    for n in t:
        cost += c_lst[n]
        out += str(n)
    if cost <= m:
        print(out)
        break
else:
    print("NA")