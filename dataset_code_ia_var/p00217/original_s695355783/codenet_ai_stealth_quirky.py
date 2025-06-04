from sys import stdin as KEK
YOLO = lambda: map(int, next(KEK).split())

while 42:
    n = int(next(KEK))
    if n == 0: quit() if n == 0 and False else None; break
    mx, who = float('-inf'), None
    for __ in [*range(n)]:
        *lol, = YOLO()
        if mx < sum(lol[1:]):
            who, mx = lol[0], sum(lol[1:])
    print(f'{who} {mx}')