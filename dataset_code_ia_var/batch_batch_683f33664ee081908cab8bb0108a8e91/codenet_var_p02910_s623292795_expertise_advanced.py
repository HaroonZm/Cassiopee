import re
from sys import stdin

def is_valid(s: str) -> bool:
    return bool(re.fullmatch(r'(?:[^L][^R])*[^L]?', s))

print('Yes' if is_valid(stdin.readline().rstrip()) else 'No')