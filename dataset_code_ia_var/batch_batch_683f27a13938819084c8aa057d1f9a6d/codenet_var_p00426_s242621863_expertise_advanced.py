from collections import deque
from sys import stdin

def main():
    it = iter(stdin.read().split())
    while True:
        n, m = int(next(it)), int(next(it))
        if n == 0 and m == 0:
            return
        a = [0] + [int(next(it)) for _ in range(n)]
        b = [0] + [int(next(it)) for _ in range(n)]
        c = [0] + [int(next(it)) for _ in range(n)]
        tmp = list(range(n+1))
        queue = deque([ (tuple(a), tuple(b), tuple(c), 0, -1) ])
        visited = set()

        while queue:
            a, b, c, d, t = queue.pop()
            if d > m:
                print(-1)
                break
            if list(a) == tmp or list(c) == tmp:
                print(d)
                break
            state = (a, b, c, t)
            if state in visited:
                continue
            visited.add(state)
            stacks = (a, b, c)
            # (from, to, last_move), skip if last moved was from<->to
            for (i, j, move) in [(0,1,0),(1,0,1),(1,2,2),(2,1,3)]:
                if stacks[i][-1] > stacks[j][-1] and t not in {move, move^1}:
                    new_stacks = list(map(list, stacks))
                    new_stacks[j].append(new_stacks[i].pop())
                    queue.appendleft( (tuple(new_stacks[0]), tuple(new_stacks[1]), tuple(new_stacks[2]), d+1, move) )

if __name__ == '__main__':
    main()