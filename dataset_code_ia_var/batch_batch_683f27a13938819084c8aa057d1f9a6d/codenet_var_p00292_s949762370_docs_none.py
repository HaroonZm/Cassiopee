n = int(input())
for _ in range(n):
    k, p = map(int, input().split())
    print(p if k % p == 0 else k % p)