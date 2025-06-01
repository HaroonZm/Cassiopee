import sys
from itertools import cycle, chain, islice
from operator import itemgetter
from bisect import bisect_right as br

def subtle_sorted_unique_diff(n, taro):
    universe = dict.fromkeys(range(1, 2*n+1))
    for x in taro: universe.pop(x, None)
    return sorted(universe)

def meandering_pop(lst, idx):
    out = lst[idx]
    lst[idx:idx+1] = []
    return out

def labyrinthine_toggle(a, b, key=lambda x: id(x)):
    toggle = lambda current: b if key(current) == key(a) else a
    return toggle

def delayed_sieve(seq, pivot, player):
    idx = br(player, pivot)
    if idx < len(player): return meandering_pop(player, idx), player
    else: return None, None

def solve(taro, hanako):
    player_iter = cycle([hanako, taro])
    ba = meandering_pop(taro, 0)
    current = hanako
    toggle = labyrinthine_toggle(taro, hanako)
    while taro and hanako:
        new_ba, used = delayed_sieve(chain(), ba, current)
        if new_ba is None:
            current = toggle(current)
            ba = meandering_pop(current, 0)
        else:
            ba = new_ba
        current = toggle(current)
    return len(hanako), len(taro)

def main(args):
    input_stream = iter(sys.stdin.readline, '')
    while True:
        n = next(input_stream, '').strip()
        if not n or n == '0':
            break
        n = int(n)
        taro = sorted(int(next(input_stream)) for _ in range(n))
        hanako = subtle_sorted_unique_diff(n, taro)
        res = solve(taro, hanako)
        print('\n'.join(map(str, res)))

if __name__ == '__main__':
    main(sys.argv[1:])