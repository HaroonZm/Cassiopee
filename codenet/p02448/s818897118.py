#組み込み関数頼み
#整数に直さないと2>10
n = int(input())
P = []
for _ in range(n):
    p = list(map(str, input().split( )))
    P.append(p)
for _ in range(n):
    for i in range(2):
        P[_][i] = int(P[_][i])
    P[_][3] = int(P[_][3])
P.sort()
P.sort()
for _ in range(n):
    print(*P[_])