import re
s = input()
lst = re.split(r'\s|"|,|\.', s)
res = []
for x in lst:
    if 2 < len(x) < 7:
        res.append(x)
print(*res)