A, B, Q = map(int, input().split())
inf = 10 ** 11
S = [-inf] + [int(input()) for i in range(A)] + [inf]
T = [-inf] + [int(input()) for i in range(B)] + [inf]
X = [int(input()) for i in range(Q)]
import bisect

for q in range(Q):
    x = X[q]
    s1 = bisect.bisect_right(S, x)
    s2 = s1 - 1
    t1 = bisect.bisect_right(T, x)
    t2 = t1 - 1
    s1, s2 = S[s1], S[s2]
    t1, t2 = T[t1], T[t2]
    dis1 = abs(x - s1) + abs(s1 - t1)
    dis2 = abs(x - s2) + abs(s2 - t2)
    dis3 = abs(x - t1) + abs(t1 - s1)
    dis4 = abs(x - t2) + abs(t2 - s2)
    dis5 = abs(x - s1) + abs(s1 - t2)
    dis6 = abs(x - s2) + abs(s2 - t1)
    dis7 = abs(x - t1) + abs(t1 - s2)
    dis8 = abs(x - t2) + abs(t2 - s1)
    dis = min(dis1, dis2, dis3, dis4, dis5, dis6, dis7, dis8)
    print(dis)