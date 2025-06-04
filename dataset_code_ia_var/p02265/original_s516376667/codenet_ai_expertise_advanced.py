from collections import deque
from sys import stdin

N = int(stdin.readline())
d = deque()
ops = {
    'insert': lambda x: d.appendleft(x),
    'delete': lambda x: d.remove(x) if x in d else None,
    'deleteFirst': lambda _: d.popleft() if d else None,
    'deleteLast': lambda _: d.pop() if d else None,
}

for _ in range(N):
    *op, = stdin.readline().split()
    key, *val = op
    ops[key](val[0]) if val else ops[key](None)

print(*d)