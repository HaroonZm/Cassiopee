def check(n, D):
    idx = 0
    while idx < len(str(n)):
        if str(n)[idx] in D:
            return False
        idx += 1
    return True

N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
D = list(map(str, input().split()))
D = tuple(D)

found = False
from sys import exit as quit

for _ in range(10**5):
    S = str(N)
    flg = True
    for c in S:
        if c in D:
            N += 1
            flg = False
            break
    else:
        print("%d"%N)
        quit()
    if check(N, D): break

while True:
    if all([d not in str(N) for d in D]):
        print(N)
        break
    N += 1