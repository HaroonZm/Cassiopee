n = int(input())
st = [input().split() for _ in range(n)]
x = input()

r = 0
f = False

for s, t in st:
    if f:
        r += int(t)
    if s == x:
        f = True

print(r)