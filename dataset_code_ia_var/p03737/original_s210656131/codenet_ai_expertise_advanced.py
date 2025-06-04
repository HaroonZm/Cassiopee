from sys import stdin

print(''.join(map(lambda s: s[0].upper(), stdin.read().split())))