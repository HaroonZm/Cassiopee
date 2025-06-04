import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())

S = input()
print(S[:len(S)-8])