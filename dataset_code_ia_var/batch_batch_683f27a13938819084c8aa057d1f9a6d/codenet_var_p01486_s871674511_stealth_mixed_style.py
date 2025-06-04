import sys
from functools import reduce
sys.setrecursionlimit(100_000)

LI = lambda: list(map(int, input().strip().split()))
LF = lambda: [float(y) for y in input().split()]
def LI_():
    return list(map(lambda z: -int(z), input().split()))
def II():
    val = input()
    return int(val)
def IF():
    return float(input())
LM = lambda fn, n: [list(map(fn, input().split())) for _ in [None]*n]

modulus = 1_000_000_007
Inf = float("inf")

def isCat(S):
    if not S:
        return True
    if S[0] != 'm' or S[-1] != 'w':
        return False
    c, i = 0, 1
    while i < len(S)-1:
        c += 1 if S[i] == 'm' else -1 if S[i] == 'w' else 0
        if c == 0:
            break
        i += 1
    j = (0 if len(S)>1 and S[1]=='e' else i)
    s1 = S[1:j+1] if j else ""
    s2 = S[j+2:-1] if j+2 < len(S)-1 else ""
    return (len(S)>1 and S[j+1:j+2]=='e') and isCat(s1) and isCat(s2)

animal = (lambda x: "Cat" if isCat(x) else "Rabbit")(input())
for word in [animal]:
    print(word)