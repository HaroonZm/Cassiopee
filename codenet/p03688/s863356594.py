# 解説AC
N = int(input())
A = [int(i) for i in input().split()]

MAXA = max(A)
MINA = min(A)

if MAXA - MINA >= 2:
    flag = False
elif MAXA - MINA == 0:
    # 全てalone -> 種類数はN
    flag = True if (A[0] == N - 1) else False
    # 全てaloneではない -> 種類数はN/2以下
    flag |= True if (2 * A[0] <= N) else False
else:
    x = A.count(MINA) # alonaな猫の匹数
    y = A.count(MAXA) # aloneではない猫の匹数
    # MAXA - x: aloneではない猫の種類数
    flag = True if (x < MAXA and 2 * (MAXA - x) <= y) else False

if flag:
    print('Yes')
else:
    print('No')