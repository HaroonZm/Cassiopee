import string
from functools import lru_cache

char_list = list(string.ascii_lowercase)
N = int(input())

@lru_cache(maxsize=None)
def base_10_to_n(X, n):
    if X <= 0:
        return ''
    X -= 1
    return base_10_to_n(X // n, n) + char_list[X % n]

print(base_10_to_n(N, 26))