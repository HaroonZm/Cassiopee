B, M, S = 13, 9, 5
dx = [0, 0, 1, 0, -1, 1, 1, -1, -1, 0, 2, 0, -2]
dy = [0, -1, 0, 1, 0, -1, 1, 1, -1, 2, 0, -2, 0]
import itertools

n = input()
cloth = []
for u in xrange(10):
    cloth.append(map(int, raw_input().split(" ")))
su = sum([sum(cloth[i]) for i in xrange(10)])
ink_sets = [list(a) for a in itertools.combinations_with_replacement([0, 13, 9, 5], n) if sum(a) == su]
dic = {B:3, M:2, S:1}

res = False
for ink_set in ink_sets:
    stack = []
    c = []
    for line in cloth:
        c.append(list(line))
    inks = list(ink_set)
    states = []
    states.append(([[c[i][j] for j in range(10)] for i in range(10)], list(inks), 0, []))
    found = False
    while states:
        state = states.pop()
        cur_cloth, ink_set, cur, ans = state
        if len(ink_set) == 0:
            res = ans
            found = True
            break
        while cur < 100 and cur_cloth[cur/10][cur%10] == 0:
            cur += 1
        for ink in set(ink_set):
            for i in xrange(ink):
                cx = cur % 10 + dx[i]
                cy = cur / 10 + dy[i]
                if 0 <= cx < 10 and 0 <= cy < 10 and cur_cloth[cy][cx] > 0:
                    ok = True
                    for j in xrange(ink):
                        nx = cx + dx[j]
                        ny = cy + dy[j]
                        if not(0 <= nx < 10 and 0 <= ny < 10) or cur_cloth[ny][nx] <= 0:
                            ok = False
                            break
                    if ok:
                        ncloth = [[cur_cloth[y][x] for x in range(10)] for y in range(10)]
                        for j in xrange(ink):
                            ncloth[cy + dy[j]][cx + dx[j]] -= 1
                        ninks = list(ink_set)
                        ninks.remove(ink)
                        nans = list(ans)
                        nans2 = list(nans)
                        nans2.append([cx, cy, ink])
                        states.append((ncloth, ninks, cur, nans2))
    if found:
        break

for r in res:
    print "{} {} {}".format(r[0], r[1], dic[r[2]])