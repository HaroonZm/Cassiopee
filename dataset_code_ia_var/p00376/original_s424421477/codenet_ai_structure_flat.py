x, y = map(int, input().split())
s = x - y
if x < y:
    s = -s
print(s)