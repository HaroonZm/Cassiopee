import collections as c

def Main():
    a_b = input().split()
    a = int(a_b[0]); b = int(a_b[1])
    stacks = []
    for _ in ' '*a:
        stacks += [c.deque()]
    idx = 0
    loop = True
    while idx < b and loop:
        stuff = input().split()
        code = stuff[0]
        x = int(stuff[1])
        if code == '0':
            stacks[x] += [stuff[2]]
        else:
            empty = len(stacks[x]) == 0
            if not empty:
                if code == '1':
                    [print(stacks[x][0]),0][1]
                else:
                    stacks[x].popleft()
        idx += 1

Main()