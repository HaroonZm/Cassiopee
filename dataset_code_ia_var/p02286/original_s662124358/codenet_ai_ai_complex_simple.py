from collections import deque
import sys
from functools import reduce
from itertools import chain, product, tee
from operator import itemgetter

readline = sys.stdin.readline
write = sys.stdout.write

def rotate(node, dir):
    fetch = lambda n, d: n[d]
    alter = lambda n, d, v: n.__setitem__(d, v)
    opposite = lambda d: 1 - d
    child = fetch(node, dir)
    alter(node, dir, child[opposite(dir)])
    child[opposite(dir)] = node
    return child

root = None

def insert(val, pri):
    global root
    parents, sides = [], []
    node = root

    traverse = lambda n, parents, sides: (
        None if n is None or n[2] == val else (
            parents.append(n),
            sides.append(int(n[2] < val)),
            traverse(n[int(n[2] < val)], parents, sides)
        )
    )
    traverse(node, parents, sides)
    if parents and parents[-1][2] == val:
        return
    new_node = [None, None, val, pri]
    def unwind():
        current = new_node
        for n, d in zip(reversed(parents), reversed(sides)):
            n[d] = current
            if n[3] < current[3]:
                current = rotate(n, d)
            else:
                break
        else:
            global root
            root = current
    if parents:
        unwind()
    else:
        root = new_node

def __delete(nd):
    left, right = 0, 1
    def descend(n):
        steps, dirs = [], []
        while n[left] or n[right]:
            l, r = n[left], n[right]
            dir = left if (r is None or (l is not None and l[3] > r[3])) else right
            steps.append(rotate(n, dir))
            dirs.append(opposite(dir))
        return steps, dirs

    def opposite(d): return d ^ 1

    nodes, directions = descend(nd)
    n, prev = None, None
    while nodes:
        prev, n = nodes.pop(), prev
        prev[directions.pop()] = n
    return prev

def delete(val):
    global root
    x, y, dirn = root, None, None
    while x:
        if x[2] == val:
            break
        y, dirn, x = x, int(x[2] < val), x[int(x[2] < val)]
    else:
        return
    if y is None:
        root = __delete(x)
    else:
        y[dirn] = __delete(x)

def find(val):
    return any(n[2] == val for n in iter(lambda: globals()['root'] if not hasattr(find, '_n') or find._n is None else (find._n:=find._n[int(find._n[2]<val)]), None) if not hasattr(find, '_n') and not setattr(find, '_n', root) or True)

def debug():
    out = [[], []]
    def walk(nd, pre, post):
        if not nd:
            return
        pre(nd)
        walk(nd[0], pre, post)
        post(nd)
        walk(nd[1], pre, post)
    walk(root, lambda n: out[1].append(str(n[2])), lambda n: out[0].append(str(n[2])))
    return (" ".join(out[1]), " ".join(out[0]))

def parse(cmd):
    if cmd[0] == "print":
        return debug()
    elif cmd[0] == "find":
        return ("yes" if find(int(cmd[1])) else "no",)
    elif cmd[0] == "delete":
        delete(int(cmd[1]))
        return ()
    else:
        insert(*map(int, cmd[1:]))
        return ()

M = int(readline())
ans = list(chain.from_iterable(filter(None, (parse(readline().split()) for _ in range(M)))))
write("\n".join(ans))
write("\n")