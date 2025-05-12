from collections import defaultdict
d = defaultdict(lambda : "no such property")

check, *yaml = list(open(0))
before = []
beforei = []
ka = defaultdict(lambda :-1)
bv = -1
for y in yaml:
    y = y.split(":")
    vacant = y[0].count(" ")
    if bv >= vacant:
        for num,b in enumerate(beforei):
            if b == vacant:
                break
        before = before[:num]
        beforei = beforei[:num]
    bv = vacant
    before.append(y[0].strip(" "))
    beforei.append(bv)
    x = y[1][1:-1]
    d[tuple(before)] = "object" if x == "" else "string \""+x+"\""
ans = tuple(check.strip("\n").split(".")[1:])
print(d[ans])