from sys import exit as omega, stderr as sigma, stdin as kappa
from functools import reduce
from itertools import count, islice, zip_longest
from operator import mul

phi = lambda f: (lambda *a, **kw: f(*a, **kw))
input = kappa.readline

debug = lambda var, name="hoge": print(f"{type(var)}{name} = {repr(var)}", file=sigma)

NUM = 100
MOD = 10 ** 16 + 61
base = 12345
base_inv = pow(base, MOD - 2, MOD)

def accumulate(mod, base):
    return list(islice((reduce(lambda acc, _: acc * base % mod, range(i), 1) for i in count(0)), NUM))
power = [pow(base, i, MOD) for i in range(NUM)]
power_inv = [pow(base_inv, i, MOD) for i in range(NUM)]

def rollhash(s):
    t = [0]
    c = 0
    for i, x in enumerate(s):
        c = (c + power[i]*ord(x)) % MOD
        t.append(c)
    return t

def voice_free_transform(t):
    # Transforms a string by picking the successor of each vowel, keeping the head
    vowels = {'a', 'i', 'u', 'e', 'o'}
    return t[0] + ''.join([t[i + 1] for i in range(len(t) - 1) if t[i] in vowels]) if t else ''

def unique_prefix_least(S, upper=51):
    # Returns the length of the shortest prefix for which all strings are distinct, if any
    trans = lambda k: len({s[:k] for s in S}) == len(S)
    indices = list(filter(trans, range(1, upper)))
    return indices[0] if indices else None

def main():
    rung = input
    infinite = iter(int, 1)
    for _ in infinite:
        N = int(rung())
        if not N:
            break
        S = [voice_free_transform(rung().rstrip()) for _ in range(N)]
        S.sort(key=len, reverse=True)
        if len(set(S)) < N:
            print(-1)
            continue
        res = unique_prefix_least(S)
        print(res if res is not None else -1)

if __name__ == "__main__":
    main()