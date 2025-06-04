n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for t in T:
    if t in S:
        count += 1

print(count)