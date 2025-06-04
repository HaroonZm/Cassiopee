import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# あいずまるの手持ちのウマウマ棒の本数
count = 0
# 盗んだ探偵の人数
res = 0

# 盗む順番の最適化を考える
# ・はじめは手持ち0で最初の1人目は盗める（特別ルール）
# ・盗んだ棒の本数を手持ちに加え、3本以上あれば3本ずつ食べて減らす
# ・手持ちが0になるとそれ以上盗めない

# これを最大人数分繰り返すには、
# aの順番を最適化する必要がある。
# 問題のキーは、「3本食べる」条件なので、
# 手持ちの棒の本数を mod 3 で管理するとよい。

# まずaを mod 3 の値でグループわけしよう。
mod0 = []
mod1 = []
mod2 = []
for x in a:
    if x % 3 == 0:
        mod0.append(x)
    elif x % 3 == 1:
        mod1.append(x)
    else:
        mod2.append(x)

# 筋道：
# 最初は手持ち0
# 盗む順番としては mod1 と mod2 の棒をバランスよく盗るのがよい
# mod0 の棒は盗むと手持ちが0になるため、次が盗めなくなるので最後に盗む
# 例外としては、最初に1個だけ盗むとき、mod0は盗めるかもしれないが0になるので終了。

# 盗む順番は以下の方針：
# 1. mod1 と mod2 を交互に盗む（盗める順）
# 2. 最初は mod1 か mod2 のどちらかから盗む（0スタートでもok）
# 3. mod0 は一回盗むだけなら可能だが、盗んだら手持ち合計は mod3=0になりそこで終わる
# 4. なので、mod0 は後回しにする。

# mod1, mod2は効率よく盗みたいので大きい順に並べる（大きいのを先に盗むと手持ちが増え維持しやすい）
mod1.sort(reverse=True)
mod2.sort(reverse=True)
mod0.sort(reverse=True)

# 手持ちの棒の mod3 の状態を管理
# 状態遷移が重要なので3パターン作って試す

# それぞれmod1から始める、mod2から始める、mod0から始める場合、の最大値を求める関数を作る

def try_steal(first_group, other_group):
    h = 0  # 手持ちの棒の本数
    cnt = 0
    f_idx = 0
    o_idx = 0
    turn = 0  # 0: first_group, 1: other_group

    n_f = len(first_group)
    n_o = len(other_group)

    # 最初は0本でも盗める例外ありの一回目
    if n_f > 0:
        h += first_group[0]
        cnt += 1
        f_idx = 1
        # 食べる処理
        while h >= 3:
            h -= 3
    else:
        return 0

    turn = 1
    while True:
        if turn == 0:
            # first_groupから盗む
            if f_idx >= n_f:
                break
            if h == 0:
                break
            h += first_group[f_idx]
            cnt += 1
            f_idx +=1
            while h >=3:
                h -=3
            turn =1
        else:
            # other_groupから盗む
            if o_idx >= n_o:
                break
            if h ==0:
                break
            h += other_group[o_idx]
            cnt +=1
            o_idx +=1
            while h>=3:
                h-=3
            turn=0
    return cnt

res = 0

# mod1とmod2を使って可能な最大人数を探索
# mod1から始めてmod2と交互
res = max(res, try_steal(mod1, mod2))

# mod2から始めてmod1と交互
res = max(res, try_steal(mod2, mod1))

# mod0は盗むと0本に戻るから、盗んだら終わる
# ただし最初は0本でも盗めるので、最初の一人として盗んでみる
if len(mod0) > 0:
    # 最初にmod0の探偵から盗む
    # 1人盗める
    temp = 1
    # その後手持ちは0になるので盗めなくなる
    res = max(res, temp)

# それ以外の人たちも盗めるか試すために
# mod1とmod2の両方から盗むパターンで残りがいるか検証を加えても良いが、
# 問題の性質上交互に盗むしか利得を最大化できない。

print(res)