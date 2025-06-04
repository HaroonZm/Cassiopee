l, n = input().split()
l = int(l)
n = int(n)
s = input()
oocnt = 0
i = 0
while i < len(s) - 1:
    if s[i] == 'o' and s[i+1] == 'o':
        oocnt = oocnt + 1
    i = i + 1
total_oocnt = 0
j = 0
while j < n:
    total_oocnt = total_oocnt + oocnt
    oocnt = oocnt * 2
    j = j + 1
result = 3 * total_oocnt + l
print(result)