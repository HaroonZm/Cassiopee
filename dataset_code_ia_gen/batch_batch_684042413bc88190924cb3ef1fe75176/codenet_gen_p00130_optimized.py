import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().strip()
    tokens = s.replace('<-', ' <- ').replace('->', ' -> ').split()
    # tokens alternent: 車両, 移動, 車両, 移動, 車両, ...

    linked = dict()  # 車両 -> { 'prev': 前の車両, 'next': 次の車両 }
    for i in range(0, len(tokens), 2):
        car = tokens[i]
        if car not in linked:
            linked[car] = {'prev': None, 'next': None}

    def link(a, b, dir):
        # dir == '->' : aの後ろにb (a.next = b, b.prev = a)
        # dir == '<-' : aの前にb (a.prev = b, b.next = a)
        if dir == '->':
            linked[a]['next'] = b
            linked[b]['prev'] = a
        else:
            linked[a]['prev'] = b
            linked[b]['next'] = a

    for i in range(1, len(tokens)-1, 2):
        a = tokens[i-1]
        dir = tokens[i]
        b = tokens[i+1]
        link(a, b, dir)

    # 先頭車両を探す（prevがNoneの車両）
    start = None
    for c in linked:
        if linked[c]['prev'] is None:
            start = c
            break

    res = []
    cur = start
    while cur is not None:
        res.append(cur)
        cur = linked[cur]['next']
    print(''.join(res))