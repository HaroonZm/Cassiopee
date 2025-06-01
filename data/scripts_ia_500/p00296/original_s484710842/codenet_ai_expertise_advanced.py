n = int(input())
s = list(range(n))
a = list(map(int, input().split()))
b = 0
for i in a:
    b = (b - i if i % 2 else b + i) % len(s)
    s.pop(b)
r = map(int, input().split())
s_set = set(s)
print(*(1 if x in s_set else 0 for x in r), sep='\n')