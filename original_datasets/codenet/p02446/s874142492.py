from sys import stdin

n = int(stdin.readline())
l = list(stdin.readline().split())
l = list(dict.fromkeys(l))
print(' '.join(l))