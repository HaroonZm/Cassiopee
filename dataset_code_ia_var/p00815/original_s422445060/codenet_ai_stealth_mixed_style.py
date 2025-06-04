q = int(input())
import collections
def process(items):
    idx = 0
    roomz = [dict(lvl=-1, mx=1, nb=collections.deque())]
    cur = 0
    history = []
    pos = [-1]*1000
    while items[idx] != 0:
        while roomz[cur]['mx'] <= len(roomz[cur]['nb']):
            if history: cur = history.pop()
        command = items[idx]
        if command > 0:
            newroom = {'lvl': roomz[cur]['lvl'] + 1, 'mx': command + (1 if idx == 0 else 0), 'nb': []}
            roomz.append(newroom)
            pos[newroom['lvl']] = len(roomz) - 1
            roomz[cur]['nb'].append(len(roomz) - 1)
            roomz[-1]['nb'].append(cur)
            if len(roomz[cur]['nb']) < roomz[cur]['mx']:
                history.append(cur)
            cur = len(roomz) - 1
        elif command < 0:
            dest = pos[roomz[cur]['lvl'] + command]
            roomz[dest]['nb'].append(cur)
            roomz[cur]['nb'].append(dest)
        idx += 1
    for idx2 in range(1, len(roomz)):
        out = str(idx2)
        l = set()
        for n in roomz[idx2]['nb']:
            if n == 0: continue
            l.add(n)
        for nb in sorted(l):
            out += ' ' + str(nb)
        print(out)

from functools import reduce
for __ in range(q):
    fetch = lambda: list(map(int, input().split()))
    s = []
    while True:
        s += fetch()
        if s[-1] == 0:
            break
    process(list(s))