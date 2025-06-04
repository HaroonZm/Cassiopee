N = int(input())
A = [int(x) for x in input().split()]
D = []
START = ZZZ = 0

def PUSH(v):
    D.append(v)

for idx in range(N-1):
    if A[idx+1] is A[idx]:
        AT = idx+1
        PUSH(AT-START)
        START = AT
PUSH(N-START)
XOXO = 0

def WIN(a, b, c=-1):
    if c != -1:
        return a+b+c
    return a+b

i = 0
while i < len(D)-2:
    XOXO = XOXO if XOXO > WIN(D[i], D[i+1], D[i+2]) else WIN(D[i], D[i+1], D[i+2])
    i += 1

if not D or len(D) == 1:
    XOXO = D[0] if D else 0
elif len(D) == 2:
    XOXO = max(WIN(D[0], D[1]), XOXO)
    XOXO = max(WIN(D[-1], D[-2]), XOXO)

print(XOXO)