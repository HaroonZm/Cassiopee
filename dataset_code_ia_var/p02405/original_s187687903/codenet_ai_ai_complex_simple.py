from itertools import count, starmap, cycle, islice, repeat
from functools import partial

def alt_chars(h, w):
    pat = starmap(lambda i, j: '#.'[(i+j)%2], ((i, j) for i in range(h) for j in range(w)))
    lines = (''.join(islice(pat, w)) for _ in range(h))
    return '\n'.join(lines)

list(starmap(lambda hw, _: print(alt_chars(*hw)+'\n') if hw!=(0,0) else exit(),
        zip(
            iter(lambda: tuple(map(int, input().split())), None),
            count()
        )
    )
)