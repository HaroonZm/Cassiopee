from itertools import cycle, islice, repeat, count, takewhile

def elaborate_checkerboard():
    get = lambda:tuple(map(int, input().split()))
    while True:
        h, w = get()
        if not sum((h,w)):
            break
        chess = (
            ''.join(
                next(c)
                for _ in range(w)
            )
            for c in (
                cycle(['#','.']) if r%2==0 else cycle(['.','#'])
                for r in range(h)
            )
        )
        print('\n'.join(chess), end='\n\n')

elaborate_checkerboard()