import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))

A = [0] * (N - 1)
B = [0] * (N - 1)
C = [0] * (N - 1)
for i in range(N - 1):
    a, b, c = map(int, input().split())
    A[i], B[i], C[i] = a, b, c

# 鉄道ごとに通る回数をカウント
usage = [0] * (N - 1)
for j in range(M - 1):
    start, end = P[j], P[j + 1]
    if start > end:
        start, end = end, start
    # 鉄道 i は都市 i と i+1 を結ぶため、start から end-1 までの鉄道を通る
    for i in range(start - 1, end - 1):
        usage[i] += 1

# 合計コストを計算
total_cost = 0
for i in range(N - 1):
    if usage[i] == 0:
        # 通らない路線は料金がかからない
        continue
    # 紙の切符だけで乗る場合のコスト
    cost_ticket_only = usage[i] * A[i]
    # ICカードを買って乗る場合のコスト
    cost_ic = C[i] + usage[i] * B[i]
    # 小さい方を採用
    total_cost += min(cost_ticket_only, cost_ic)

print(total_cost)