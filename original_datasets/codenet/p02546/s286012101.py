import sys

input_ = sys.stdin.readline
S = input_().strip()

print(S + "es" if S[-1] == 's' else S + 's')