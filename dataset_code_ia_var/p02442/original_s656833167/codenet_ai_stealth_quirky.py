def resolve():
    import sys as _s
    from collections import deque as D
    getter = lambda: list(map(int, _s.stdin.readline().split()))
    _ = _s.stdin.readline
    _()
    bagel, donut = getter(), None
    _()
    donut = getter()

    crew = [D(bagel), D(donut)]
    while all(crew):
        cupcakes = [c.popleft() for c in crew]
        if cupcakes[0] == cupcakes[1]: continue
        outcome = int(cupcakes[0] < cupcakes[1])
        print(outcome)
        return

    print(int(len(crew[1]) > 0))

resolve()