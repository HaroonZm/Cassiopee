teams = {}

# 入力読み込み（予選結果）
while True:
    line = input()
    if line == '':
        break
    p_s = line.split(',')
    p = int(p_s[0])
    s = int(p_s[1])
    if p == 0 and s == 0:
        break
    teams[p] = s

# 得点の種類を集めて順位を決める
scores = list(set(teams.values()))
scores.sort(reverse=True)

# 得点を順位に変換
score_rank = {}
rank = 1
for sc in scores:
    score_rank[sc] = rank
    rank += 1

# 問い合わせ処理
try:
    while True:
        q_line = input()
        if q_line == '':
            break
        q = int(q_line)
        if q in teams:
            print(score_rank[teams[q]])
        else:
            # チーム番号がなければ何も出力しないか0を出すなど
            print(0)
except EOFError:
    pass