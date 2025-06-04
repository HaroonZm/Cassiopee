# 入力を受け取る
N, M = map(int, input().split())  # 競技数Nと委員数M

# 競技の開催に必要な費用リスト
A = [int(input()) for _ in range(N)]

# 委員の審査基準リスト
B = [int(input()) for _ in range(M)]

# 各競技が獲得した票数を管理（0で初期化）
votes = [0] * N

# 各委員について処理を行う
for bj in B:
    # この委員が投票する競技のインデックスを探す
    # 競技はi番目に面白い順になっているため、面白さの小さい順（i=0から）
    for i in range(N):
        if A[i] <= bj:
            # 最も面白いかつ開催費用が審査基準以下の競技を発見し、1票投じる
            votes[i] += 1
            break  # 1つ投票したら同じ委員は投票終了

# 最大票数を獲得した競技の番号（インデックス+1）を求める
max_votes = max(votes)
winner = votes.index(max_votes) + 1

# 結果を出力
print(winner)