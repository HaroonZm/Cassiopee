M, N = map(int, input().split())
A = list(map(int, input().split()))

changes = 0
for i in range(1, N):
    if A[i] == A[i-1]:
        changes += 1
        # 変更するけど具体的な数値は与えられていないので適当に変更したことにする
        # 実際はここで別のTシャツを選ぶ必要があるが問題では最小変更数のみを求める
        A[i] = -1  # ダミー値

print(changes)