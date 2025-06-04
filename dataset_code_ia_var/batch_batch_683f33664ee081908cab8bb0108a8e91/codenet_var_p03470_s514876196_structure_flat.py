n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
s = set()
for x in d:
    s.add(x)
print(len(s))