l,n = map(int,input().split())
s = input()
c = 0

for i in range(l - 1):
    if s[i:i + 2] == "oo":
        c += 1
while n:
    l += c * 3
    c *= 2
    n -= 1
print(l)