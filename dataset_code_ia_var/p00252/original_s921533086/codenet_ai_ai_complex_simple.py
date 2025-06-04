from functools import reduce
from operator import xor, and_

# Lecture et transformation
b = list(map(int, raw_input().split()))

# Utilisation de reduce et map+xor pour capturer les cas
# (équivalent à: "Ou exclusive sur les 3, ET sur les 2 premiers, Négation du 3ème")
result = (
    'Open' if any([
        reduce(and_, map(bool, b[:2])) and not b[2],
        not reduce(and_, map(bool, b[:2])) and b[2] and not (b[0] ^ b[1])
    ]) else 'Close'
)

print result