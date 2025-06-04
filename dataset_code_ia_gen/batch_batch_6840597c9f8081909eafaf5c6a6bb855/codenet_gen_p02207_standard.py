import sys
import bisect
input = sys.stdin.readline

N = int(input())
T, A = zip(*[tuple(map(int, input().split())) for _ in range(N)])

# Calculer le facteur multiplicatif cumulative pour chaque séisme
# Performance se multiplie par (1 - 0.1 * p) = (1 - 0.1 * A_i)
prefix = [1.0]
for a in A:
    prefix.append(prefix[-1] * (1 - 0.1 * a))

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    # Trouver les indices de séismes dans l'intervalle [L,R]
    li = bisect.bisect_right(T, L)
    ri = bisect.bisect_right(T, R)
    # Calcul de la performance apres les seismes dans l'intervalle
    perf = 1e9 * (prefix[ri] / prefix[li])
    print(perf)