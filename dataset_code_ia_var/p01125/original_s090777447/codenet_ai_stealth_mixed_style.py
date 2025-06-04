def between(a, b, v):
    # Old style, compact, one-liner style within control
    return min(a, b) <= v <= max(a, b)

from collections import deque
import sys

def main():
    pos = [10, 10]
    while 1:
        result = 'No'
        N = int(input())
        if N == 0:
            break
        lst = []
        for _ in range(N):
            p = tuple(map(int, input().split()))
            lst.append(p)
        M = int(input())
        cmdList = []
        for _ in range(M):
            # Mix: comprehension, mutability, tuple, object
            cmd = input().split()
            direction, steps = cmd[0], int(cmd[1])
            if result == 'Yes':
                continue
            dx = dy = 0
            if direction == 'E': dx = steps
            elif direction == 'W': dx = -steps
            elif direction == 'N': dy = steps
            elif direction == 'S': dy = -steps
            else: raise Exception
            rm = []
            for xj, yj in lst:
                if dx != 0 and yj == pos[1] and between(0, dx, xj - pos[0]):
                    rm.append((xj, yj))
                elif dy != 0 and xj == pos[0] and between(0, dy, yj - pos[1]):
                    rm.append((xj, yj))
            for x, y in rm:
                try:
                    lst.remove((x, y))
                except: pass
            # Lambda + mutating state in-place, procedural, functional
            [pos.__setitem__(0, pos[0]+dx) if dx else pos.__setitem__(1, pos[1]+dy)]
            if not lst:
                result = 'Yes'
        print(result)

main()