from functools import reduce
from operator import add, mul
from itertools import chain, combinations, starmap, product, islice, count as itercount

make_alphabet = lambda now_alphabet, alphabet: list(map(lambda pair: ''.join(pair), product(now_alphabet, alphabet)))

a = int(__import__('builtins').input())
b = list(islice((__import__('builtins').input() for _ in iter(int,1)), a))
alphabet = list(map(chr, range(97, 123)))
now_alphabet = alphabet[:]
ct = -1
found = False

while not found:
    ct += 1
    letter = list(chain.from_iterable(starmap(lambda w, c: [w[i:i+1+c] for i in range(len(w)-c)], [(word, ct) for word in b])))
    rem = sorted(set(now_alphabet) - set(letter))
    next(iter(rem)) and print(rem[0]) or None if rem else None
    found = len(rem) > 0
    now_alphabet = make_alphabet(now_alphabet, alphabet) if not found else now_alphabet