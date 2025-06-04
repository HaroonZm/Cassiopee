import sys

from functools import partial

sys.setrecursionlimit(10**6)

def input_stream(): return sys.stdin.readline()
def LI(): return list(map(int, input_stream().split()))
def I(): return int(input_stream())
def LS(): return list(map(list, input_stream().split()))
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

mod = 10**9 + 7

def is_subsequence(sub, seq):
    it = iter(seq)
    return all(c in it for c in sub)

def B():
    s = S()
    t = S()
    even_chars = s[::2]
    odd_chars = s[1::2]

    if is_subsequence(even_chars, t) or is_subsequence(odd_chars, t):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    B()