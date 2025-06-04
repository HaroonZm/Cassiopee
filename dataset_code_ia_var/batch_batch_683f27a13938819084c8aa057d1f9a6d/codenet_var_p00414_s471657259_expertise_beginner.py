l, n = input().split()
l = int(l)
n = int(n)
s = input()
c = 0
i = 0

while i < l - 1:
    if s[i] == 'o' and s[i+1] == 'o':
        c = c + 1
    i = i + 1

while n > 0:
    l = l + c * 3
    c = c * 2
    n = n - 1

print(l)