n = int(input())
S = [int(_) for _ in input().split()]
q = int(input())
T = [int(_) for _ in input().split()]

cnt = 0

for t in T:
    if t in S:
        cnt += 1

print(cnt)