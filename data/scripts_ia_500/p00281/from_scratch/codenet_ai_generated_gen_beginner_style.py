N, M = map(int, input().split())

# 職人ごとに工事の種類と回数を記録するリストを作る（1-indexにして扱いやすくするためN+1）
works = [[] for _ in range(N+1)]

while True:
    s, t, e = map(int, input().split())
    if s == 0 and t == 0 and e == 0:
        break
    # s番目の職人がt番目の工事をe回やったことを記録する
    works[s].append((t, e))

L = int(input())
for _ in range(L):
    b = list(map(int, input().split()))
    # 各職人の給料を出す
    result = []
    for i in range(1, N+1):
        salary = 0
        for (t, e) in works[i]:
            # 単価は0-indexなので t-1に注意
            salary += e * b[t-1]
        result.append(str(salary))
    print(" ".join(result))