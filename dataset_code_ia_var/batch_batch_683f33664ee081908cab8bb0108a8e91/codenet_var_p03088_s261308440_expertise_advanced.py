from collections import defaultdict
from functools import lru_cache

n = int(input())
mod = 10**9 + 7
chars = 'ACGT'
states = defaultdict(int)
states['XXX'] = 1

@lru_cache(maxsize=None)
def acceptable(t: str) -> bool:
    # Check if any AGC can be formed by single swap in last 4 chars
    for pos in range(4):
        arr = list(t)
        if pos > 0:
            arr[pos-1], arr[pos] = arr[pos], arr[pos-1]
        if 'AGC' in ''.join(arr):
            return False
    return True

for _ in range(n):
    new_states = defaultdict(int)
    for s, cnt in states.items():
        for c in chars:
            nexts = s[1:] + c
            if acceptable(s + c):
                new_states[nexts] = (new_states[nexts] + cnt) % mod
    states = new_states

print(sum(states.values()) % mod)