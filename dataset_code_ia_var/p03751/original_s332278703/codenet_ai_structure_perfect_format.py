n = int(input())
s = [input() for _ in range(n)]
b = input()
ans = []

def change(s, az):
    res = ""
    for i in s:
        if i != "?":
            res += i
        else:
            res += az
    return res

a = [b]
z = [b]
for i in s:
    a.append(change(i, "a"))
    z.append(change(i, "z"))
a.sort()
z.sort()
for i in range(n + 1):
    if a[i] == b:
        ans.append(i + 1)
        break
for i in range(1, n + 2):
    if z[-i] == b:
        ans.append(n + 2 - i)
        break
ans.sort()
anss = str(ans[0])
for i in range(1, ans[1] - ans[0] + 1):
    anss += " " + str(ans[0] + i)
print(anss)