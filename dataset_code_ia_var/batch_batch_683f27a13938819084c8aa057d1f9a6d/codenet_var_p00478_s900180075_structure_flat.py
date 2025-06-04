t = input()
n = int(input())
s = 0
for _ in range(n):
    x = input()
    if t in x + x:
        s += 1
print(s)