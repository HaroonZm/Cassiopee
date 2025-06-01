# JOI大学のM教授の課題未提出者特定プログラム

# クラスは受講生30人（番号1～30）がいて、
# 28人が課題を提出している。
# 提出した学生の番号から提出していない2人を見つける問題。

# --- アプローチ ---
# 1. 1～30の番号の集合を作成する。
# 2. 入力された28人の提出者番号をセットにする。
# 3. 1の集合から2の集合を引くことで未提出者の集合が得られる。
# 4. 未提出者の集合の2つの番号をソートして出力する。

# この方法は入力の順序に依存せず、計算も高速。

# 以下、実装。

submitted = set()  # 提出者の番号を保持するセット

# 28行の入力を読み込む
for _ in range(28):
    num = int(input())
    submitted.add(num)

# 1～30の番号の集合を作る
all_students = set(range(1, 31))

# 未提出者の集合を求める
not_submitted = all_students - submitted

# 2人の未提出者番号をソートしてリスト化
not_submitted_sorted = sorted(not_submitted)

# 小さい方を1行目に、大きい方を2行目に出力
print(not_submitted_sorted[0])
print(not_submitted_sorted[1])