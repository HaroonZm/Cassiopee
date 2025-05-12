n = int(input())
s = set()
l = list(map(int, input().split()))
for i in range(n):
    s.add(l[i])
print(len(s))