N = int(input())
s = set()
for i in range(N):
    a = input().split()
    a = [int(x) for x in a]
    a.sort()
    s.add((a[0], a[1]))
print(N - len(s))