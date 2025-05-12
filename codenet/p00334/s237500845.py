N = int(input())
s = set()
for i in range(N):
    s.add(tuple(sorted(map(int, input().split()))))
print(N-len(s))