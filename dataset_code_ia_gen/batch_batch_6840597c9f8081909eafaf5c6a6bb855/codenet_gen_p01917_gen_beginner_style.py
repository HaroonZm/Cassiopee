N = int(input())
r = list(map(int, input().split()))
units = [list(map(int, input().split())) for _ in range(N)]

def get_scores(vals):
    # valsはN個の値
    sorted_vals = sorted(vals, reverse=True)
    scores = [0]*N
    rank = 1
    i = 0
    while i < N:
        val = sorted_vals[i]
        j = i+1
        while j < N and sorted_vals[j] == val:
            j += 1
        # iからj-1までが同率順位rank
        for k in range(i, j):
            # 元のindexesを探す
            idx = vals.index(val)
            # vals.index(val) は最初の発見のみなので、似た値複数ある場合は工夫が必要
            # そこで全て探す
        # 上記のやり方は間違いなので変える
        i = j

    # 上のコードでは元のindexを取るのに問題があるので辞書で対応する
def get_rank_scores(vals):
    sorted_vals = sorted(vals, reverse=True)
    pos = {}
    i = 0
    rank = 1
    scores = [0]*N
    while i < N:
        val = sorted_vals[i]
        j = i
        while j < N and sorted_vals[j] == val:
            j += 1
        for x in range(N):
            if vals[x] == val:
                scores[x] = r[rank-1]
        rank += (j - i)
        i = j
    return scores

def total_score(s, p, c):
    smile_scores = get_rank_scores(s)
    pure_scores = get_rank_scores(p)
    cool_scores = get_rank_scores(c)
    total = [smile_scores[i]+pure_scores[i]+cool_scores[i] for i in range(N)]
    return total

# ドサンコスノーの初期スコア
s_vals = [units[i][0] for i in range(N)]
p_vals = [units[i][1] for i in range(N)]
c_vals = [units[i][2] for i in range(N)]
init_scores = total_score(s_vals, p_vals, c_vals)

# スノーの初期得点
snow_score = init_scores[0]

# 自分が9位ということは、順位を調べる必要がある
# 順位はスコアの中で高い順
def get_rank(scores, idx):
    sorted_scores = sorted(scores, reverse=True)
    target = scores[idx]
    rank = 1
    i = 0
    while i < N:
        val = sorted_scores[i]
        j = i
        while j < N and sorted_scores[j] == val:
            j += 1
        if val == target:
            return rank
        rank += (j - i)
        i = j
    return N

init_rank = get_rank(init_scores, 0)
if init_rank <= 8:
    print(0)
    exit()

max_inc = 1000
ans = max_inc+1

for val_type in range(3):
    # val_type: 0=s,1=p,2=c
    base_vals = [units[i][val_type] for i in range(N)]
    for inc in range(1, max_inc+1):
        new_vals = base_vals[:]
        new_vals[0] += inc
        # 今回は他の2属性は元のまま
        if val_type == 0:
            s2 = new_vals
            p2 = p_vals
            c2 = c_vals
        elif val_type == 1:
            s2 = s_vals
            p2 = new_vals
            c2 = c_vals
        else:
            s2 = s_vals
            p2 = p_vals
            c2 = new_vals
        ts = total_score(s2, p2, c2)
        rnk = get_rank(ts, 0)
        if rnk <= 8:
            if inc < ans:
                ans = inc
            break

if ans == max_inc+1:
    print("Saiko")
else:
    print(ans)