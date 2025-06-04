n = int(input())
for _ in range(n):
    k, p = map(int, input().split())
    if k % p == 0:
        print(p)
    else:
        print(k % p)