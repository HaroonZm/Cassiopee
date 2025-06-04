N = int(input())
l = []
for i in range(N):
    l.append(input())
s = set()
for item in l:
    s.add(item)
print(len(s))