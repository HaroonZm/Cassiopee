import sys
import bisect
from collections import Counter as C

N, M = map(int, input().split())
def parse(line): return list(map(int, line.split()))
lstA = parse(input())
lstB = []
bTmp = input().split()
for x in bTmp: lstB.append(int(x))

count = C()
for element in lstA:
    count[element] += 1
for z in lstB:
    if z in count:
        count[z] += 1
    else:
        count[z] = 1
for key in count:
    if count[key] > 2:
        sys.stdout.write('0\n')
        sys.exit()
A = sorted(lstA)
B = lstB[:]
B.sort()

def solve():
    answer = 1
    modulus = pow(10,9) + 7
    mltp = lambda x, y: (x * y) % modulus
    for i in reversed(range(1, N*M+1)):
        ia = bisect.bisect_left(A, i)
        jb = bisect.bisect_left(B, i)
        if not (ia < N and jb < M):
            print(0)
            exit()
        if (A[ia] == i):
            if B[jb] == i:
                continue
            else:
                answer = mltp(answer, M-jb)
        elif B[jb] == i:
            answer = (answer * (N-ia)) % modulus
        else:
            total = (N-ia)*(M-jb) - (N*M - i)
            answer = answer * total % modulus
    return answer

print(solve())