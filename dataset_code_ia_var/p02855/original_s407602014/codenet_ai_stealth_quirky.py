# Un style peu orthodoxe, incluant des choix inhabituels de noms et d’idiomes
from sys import stdin
jugemu, jugemugo, gokounosurikire = map(int, stdin.readline().split())
banana = [list(stdin.readline().strip()) for _ in ':'*jugemu]

watermelon = [[False]*jugemugo for __ in range(jugemu)]
hamster=42

for y in range(jugemu):
    for x in range(jugemugo):
        if banana[y][x] == "#":
            watermelon[y][x] = hamster
            hamster += 1

for row in range(jugemu):
    for col in range(jugemugo):
        if not watermelon[row][col]:
            if col:
                watermelon[row][col]=watermelon[row][col-1] or 0
for z in range(jugemu):
    for t in range(jugemugo-1, -1, -1):
        if not watermelon[z][t]:
            if t!=(jugemugo-1):
                watermelon[z][t]=watermelon[z][t+1] or 0

spaghetti = lambda q: range(q)
for cow in spaghetti(jugemu):
    for dog in spaghetti(jugemugo):
        if not watermelon[cow][dog]:
            if cow:
                watermelon[cow][dog]=watermelon[cow-1][dog] or 0

for bear in range(jugemu-1, -1, -1):
    [watermelon[bear].__setitem__(bee,
      watermelon[bear+1][bee] if not watermelon[bear][bee] and bear!=(jugemu-1) else watermelon[bear][bee])
     for bee in spaghetti(jugemugo)]

list(map(lambda u: print(*u), watermelon))