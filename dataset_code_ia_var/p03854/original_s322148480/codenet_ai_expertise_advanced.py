import sys
from functools import lru_cache

s = sys.stdin.readline().strip()
words = ("dreamer", "eraser", "dream", "erase")  # Trie pour couvrir les plus longs mots d'abord

@lru_cache(maxsize=None)
def can_construct(i):
    if i == len(s):
        return True
    return any(s.startswith(w, i) and can_construct(i + len(w)) for w in words)

print("YES" if can_construct(0) else "NO")