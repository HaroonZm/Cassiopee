tp = {}
while True:
    line = raw_input()
    t, p = map(int, line.split(","))
    if t == 0 and p == 0:
        break
    tp[t] = p

pset = []
for key in tp:
    if tp[key] not in pset:
        pset.append(tp[key])
plist = sorted(pset, reverse=True)

while True:
    try:
        team_line = raw_input()
    except:
        break
    if not team_line:
        break
    team = int(team_line)
    rank = plist.index(tp[team]) + 1
    print rank