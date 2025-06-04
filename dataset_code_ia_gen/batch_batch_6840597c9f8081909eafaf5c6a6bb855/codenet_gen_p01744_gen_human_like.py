import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h, w, n = map(int, input().split())
removes = [tuple(map(int, input().split())) for _ in range(n)]

# 初期状態：全ての (a,b) で a≡b (mod 2) の位置に横棒がある
# 横棒のない場所は removes にある

# 横棒の有無を管理するために集合を用いる
# 横棒があるかは (a,b) が全体候補に含まれているかつ removes に含まれていないかで判定
removed_set = set(removes)

# あみだくじの縦棒は1からwまで
# 1回の操作でiとi+1が入れ替わる横棒があるかどうか確認しながら最後までたどる

# つまり、あみだくじの最下層から上に向かって追っても結果は同じ
# ここでは上から下に順に追う
# 横棒がある→i番目とi+1番目が入れ替わる

# 全ての有効な横棒の場所は (a,b) で 1 <= a <= h, 1 <= b <= w-1, a≡b (mod 2)
# 横棒がない場所は removes にあると認識

# スキャン時にこの横棒が存在するか否かは (a,b) not in removed_set なら存在する

# ただし、高速化のため、横棒位置の情報を各段で作成するとメモリに厳しい

# 解法案：
# 各段 a に対して、最初にあった横棒は a,b (a≡b mod2) で b in [1,w-1]
# 横棒がなければ常に i は i のまま下に行く
# 横棒があれば i と i+1 は入れ替わる
#
# 各段ごとに配列を作るのは不可能なので、
# 横棒がない場合を重視して、
# ある横棒の位置がわかれば i と i+1 を入れ替えるという操作を所有

# removes は消す横棒
# 横棒は a,b (a≡b mod2)
# 全横棒数は h*(w-1)/2

# 配列で段毎の横棒位置をまとめる
# 横棒があるかどうかは除外された横棒で判定

# bottom upで、w本の縦棒の関係を管理し、操作後の配列を出す
# 横棒を消す操作は横棒をない状態に戻すだけ
# つまり、初期状態はすべての横棒がある状態
# removes の横棒は削除済

# これらはeach a に対して keys=bを管理し、bのSetを作る

# 横棒は「switches」で管理したい。各段に存在する横棒の場所と除去されたものを区別

# よって、
# switches = dict()
#  switches[a] = set of b where horizontal line exists at (a,b)
#は初期状態で全てbでb≡a mod 2なのでだけ足す
#それにremovesで除去を行う

# 探索時は段ごとにiが横棒位置とマッチしたらi<->i+1を交換

switches = {}
for a in range(1, h+1):
    switches[a] = set()
    for b in range(1, w):
        if (a % 2) == (b % 2):
            switches[a].add(b)

for a, b in removes:
    switches[a].discard(b)

for start in range(1, w+1):
    i = start
    for a in range(1, h+1):
        # この段に横棒があってiがbかb+1だと入れ替わり
        # 横棒はbとb+1をつなぐので bならiがbならb+1に移動し、
        # b+1ならbに移動する
        bset = switches[a]
        if i in bset:
            i += 1
        elif i-1 in bset:
            i -= 1
    print(i)