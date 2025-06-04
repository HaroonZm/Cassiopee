from collections import deque
from itertools import islice

def main():
    while True:
        try:
            n, m = map(int, input().split())
            if not (n or m):
                return
            # Unpack efficiently, skip first element
            a = [0, *map(int, islice(input().split(), 1, None))]
            b = [0, *map(int, islice(input().split(), 1, None))]
            c = [0, *map(int, islice(input().split(), 1, None))]

            goal = list(range(n + 1))
            # Queue state: (a, b, c, moves, prev_move)
            q = deque([(a, b, c, 0, -1)])
            # Visited states for pruning
            seen = set()

            def pack_state(a, b, c):
                return (tuple(a), tuple(b), tuple(c))

            while q:
                a, b, c, d, t = q.pop()
                state = pack_state(a, b, c)
                if state in seen:
                    continue
                seen.add(state)

                if d > m:
                    print(-1)
                    break
                if a == goal or c == goal:
                    print(d)
                    break

                moves = [
                    (a[:-1], b + [a[-1]], c, 0) if a[-1] > b[-1] and t != 1 else None, # a -> b
                    (a + [b[-1]], b[:-1], c, 1) if b[-1] > a[-1] and t != 0 else None, # b -> a
                    (a, b[:-1], c + [b[-1]], 2) if b[-1] > c[-1] and t != 3 else None, # b -> c
                    (a, b + [c[-1]], c[:-1], 3) if c[-1] > b[-1] and t != 2 else None # c -> b
                ]

                for move in filter(None, moves):
                    na, nb, nc, nt = move
                    q.appendleft((
                        na[:], nb[:], nc[:], d + 1, nt
                    ))
        except EOFError:
            return

if __name__ == '__main__':
    main()