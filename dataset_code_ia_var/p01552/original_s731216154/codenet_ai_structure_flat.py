from collections import defaultdict
d = defaultdict(lambda : "no such property")
import sys
lines = list(sys.stdin)
if lines:
    check, *yaml = lines
else:
    check = ''
    yaml = []
before = []
beforei = []
ka = defaultdict(lambda :-1)
bv = -1
for y in yaml:
    y = y.split(":")
    vacant = y[0].count(" ")
    if bv >= vacant:
        for num in range(len(beforei)):
            if beforei[num] == vacant:
                break
        before = before[:num]
        beforei = beforei[:num]
    bv = vacant
    before.append(y[0].strip(" "))
    beforei.append(bv)
    x = y[1][1:-1]
    if x == "":
        d[tuple(before)] = "object"
    else:
        d[tuple(before)] = "string \""+x+"\""
ans = tuple(check.strip("\n").split(".")[1:])
print(d[ans])