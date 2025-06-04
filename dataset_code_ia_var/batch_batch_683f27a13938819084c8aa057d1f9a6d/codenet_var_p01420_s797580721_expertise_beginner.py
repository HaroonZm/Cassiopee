from collections import deque
import sys

sys.setrecursionlimit(1000000)

def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n

# Read main parameters
NML = raw_input().split()
N = int(NML[0])
M = int(NML[1])
L = int(NML[2])

# Compute binomial coefficients (M choose k)
MC = []
for i in range(M + 1):
    mc = factorial(M) / (factorial(i) * factorial(M - i))
    MC.append(mc)

# Read object data and compute probability tables
p_list = []
P_val = []
P_sum = []

for i in range(N):
    line = raw_input().split()
    P = int(line[0])
    T = int(line[1])
    V = int(line[2])
    p_list.append((T, V))

    PP = []
    for k in range(M + 1):
        prob = float(MC[k] * (P ** k) * ((100 - P) ** (M - k))) / (100 ** M)
        PP.append(prob)
    P_val.append(list(PP))

    # Compute suffix sums for optimization
    for k in range(M, 0, -1):
        PP[k - 1] += PP[k]
    P_sum.append(PP)

def compare(obj1, obj2, k1, k2):
    t1, v1 = obj1
    t2, v2 = obj2
    left = L * (v2 - v1)
    right = v1 * v2 * (k2 * t2 - k1 * t1)
    return left < right

for i in range(N):
    answer = 0.0
    index_list = [0 for j in range(N)]
    for k1 in range(M + 1):
        result = P_val[i][k1]
        for j in range(N):
            if i == j:
                continue
            while True:
                k2 = index_list[j]
                if k2 > M:
                    result = 0.0
                    break
                if compare(p_list[i], p_list[j], k1, k2):
                    result = result * P_sum[j][k2]
                    break
                index_list[j] += 1
        answer += result
    print '%.10f' % answer