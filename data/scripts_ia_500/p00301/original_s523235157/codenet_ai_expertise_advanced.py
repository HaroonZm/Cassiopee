import os
import sys

if os.environ.get('PYDEV') == "True":
    sys.stdin = open("sample-input.txt", "rt")

N = int(input())

mapping = {0: '0', 1: '+', 2: '-'}
digits = []

while N:
    r = N % 3
    if r == 2:
        digits.append('-')
        N = N // 3 + 1
    else:
        digits.append(mapping[r])
        N //= 3

print(''.join(reversed(digits)) or '0')