import math

M = 256
while True:
    try:
        N = int(raw_input())
    except:
        break
    if N == 0:
        break
    H = float('inf')
    l = [int(x) for x in raw_input().split()]
    solution = None
    bestS = bestA = bestC = None
    Hstar = H
    for S in xrange(16):
        for A in xrange(16):
            for C in xrange(16):
                R = S
                O = []
                idx = 0
                while idx < N:
                    R = (A*R + C) % M
                    O.append((l[idx]+R) % M)
                    idx += 1
                freq = [None]*M
                for z in range(M): freq[z] = 0
                for value in O:
                    freq[value] += 1
                summ = 0.0
                for count in freq:
                    if count != 0:
                        p = 1.0 * count / N
                        summ += p * math.log(p, 2)
                entropy = -summ
                if entropy < Hstar:
                    bestS = S
                    bestA = A
                    bestC = C
                    Hstar = entropy
    print '{} {} {}'.format(bestS, bestA, bestC)