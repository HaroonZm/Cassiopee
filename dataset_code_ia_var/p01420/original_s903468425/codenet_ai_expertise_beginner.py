from collections import deque
import sys

sys.setrecursionlimit(1000000)

def get_input():
    return map(int, raw_input().split())

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

N, M, L = get_input()

# Create MC list
MC = []
for i in range(M + 1):
    MC.append(factorial(M) / (factorial(i) * factorial(M - i)))

players = []
P_values = []
P_cumsum = []

for i in range(N):
    P, T, V = get_input()
    players.append((T, V))
    proba = []
    for k in range(M + 1):
        prob = MC[k] * (P ** k) * ((100 - P) ** (M - k)) / float(100 ** M)
        proba.append(prob)
    P_values.append(list(proba))
    # Cumulative sum in reverse
    for k in range(M, 0, -1):
        proba[k - 1] += proba[k]
    P_cumsum.append(proba)

def compare(player1, player2, k1, k2):
    T1, V1 = player1
    T2, V2 = player2
    if L * (V2 - V1) < V1 * V2 * (k2 * T2 - k1 * T1):
        return True
    else:
        return False

for i in range(N):
    answer = 0.0
    idx_list = [0] * N
    for k1 in range(M + 1):
        result = P_values[i][k1]
        for j in range(N):
            if i == j:
                continue
            flag = True
            while True:
                k2 = idx_list[j]
                if k2 > M:
                    result *= 0
                    break
                if compare(players[i], players[j], k1, k2):
                    result *= P_cumsum[j][k2]
                    break
                idx_list[j] += 1
        answer += result
    print '%.10f' % answer