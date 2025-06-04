import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

N = int(input())
m = int(input())
s = input()

var_limits = {}
vars_order = []
for _ in range(m):
    v,u = input().split()
    u = int(u)
    var_limits[v] = u
    vars_order.append(v)

# 文字種判定
digits = set("0123456789")
letters = set(var_limits.keys())

# 各アルファベットの割り当て値を格納する配列（-1 は未決定）
assign = [-1]*m
var_index = {v:i for i,v in enumerate(vars_order)}

# 回文なのを利用してチェックする。左と右のペアで組み合わせをチェック。
# 片側が数字なら固定、アルファベットなら数字に置き換え可能。左右で矛盾があれば0通り。

# 左右の文字の対応関係を管理するUnion-Find的な仕組みではなく、
# 双方向チェックで制約を絞り込んで、場合分けする方法で計算。

# 置換変数ごとに制約を増やせるか考えるのは難しいので、
# ペアごとの制約に注目して、グラフを作り、連結成分ごとに場合の数を計算する。

# 各文字の位置に数字orアルファベットがある。左右で矛盾があれば0。

# 文字s[i]とs[j] (j = N-1 - i) は同じ数字になる。
# もしs[i], s[j]両方数字なら不一致なら0。
# もし片方数字で片方アルファベットなら、そのアルファベットは固定数字。
# もし両方アルファベットなら同じ数字にする制約がある（同じ変数なら自明）

# 以上から、まずペアごとに制約をチェックし、変数はグループ化する。
# 同じ変数で複数制約になる可能性あり。

# アルファベット同士の同値制約グラフ（連結成分毎に一つの変数扱い）。
# 連結成分内で決まった数字制約があれば、その数字で固定。
# 複数数字制約が矛盾してたら0。
# 数字制約がない場合、変数は各変数内で条件を満たす範囲内の数字何通りかで乗算。

# 数字が割り当てられるとき、leading zero禁止なので0の割当を条件に含む。
# ただし、問題文にleading zero不可は「置き換えた後の数字がleading zero を含まない整数」とある。
# これは各変数が1文字なので、変数が0で始まってはいけない
# つまり、変数の値は0からu_iまでの整数で、先頭文字が変数なら0のみではダメ：
# 先頭文字がその変数の場合は0で割り当てできない。

# このため、先頭文字と末尾文字に注意し、先頭文字が変数vならvの割当は0禁止。

# [実装の流れ]
# 1. 各位置iの文字は数字か変数か判別
# 2. 左右対称位置(i, N-1-i)の文字の関係を分析し、変数同士の同値制約、数字決定、矛盾チェック
# 3. 変数間同値制約でグループ化して、グループごとに数字割当の可能性を計算
# 4. 先頭文字が変数のグループで0禁止制約追加
# 5. 各変数の上限u_iから可能な数字の数を計算（0禁止なら範囲から0を除く）
# 6. 各グループ内複数変数は共通の割当数字なので、各グループで割当可能な数字の個数が答え
# 7. すべてのグループの積が答え

# union-findでグループ管理
class UnionFind:
    def __init__(self,n):
        self.par = list(range(n))
    def find(self,x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        self.par[y] = x
    def same(self,x,y):
        return self.find(x) == self.find(y)

uf = UnionFind(m)

# 変数に対して数字割当制約
# グループ単位にまとめるために以下3つを管理(各変数はm)
# group_num_constraints[root] = setした数字制約があるか（ただ一つに限定）
# group_zero_forbidden[root] = True if 先頭文字に現れて0不可
# group_u_max[root] = u_iの最大。複数変数がいたら最小化していく必要あり

group_num_constraints = dict() # root -> 固定数字（ただ一つが条件）
group_zero_forbidden = dict() # root -> True or False
group_vars = dict() # root -> list of variable indices

# sを配列化し変数ならindexに変換しつつ
arr = []
for c in s:
    if c in var_index:
        arr.append(('v', var_index[c]))
    else:
        arr.append(('d', c))

# 文字列の左右のペアで検査
for i in range(N//2):
    j = N - 1 - i
    c1t,c1v = arr[i]
    c2t,c2v = arr[j]
    if c1t == 'd' and c2t == 'd':
        if c1v != c2v:
            print(0)
            exit()
    elif c1t == 'v' and c2t == 'd':
        root = uf.find(c1v)
        d = int(c2v)
        if root in group_num_constraints:
            if group_num_constraints[root] != d:
                print(0)
                exit()
        else:
            group_num_constraints[root] = d
    elif c1t == 'd' and c2t == 'v':
        root = uf.find(c2v)
        d = int(c1v)
        if root in group_num_constraints:
            if group_num_constraints[root] != d:
                print(0)
                exit()
        else:
            group_num_constraints[root] = d
    else:
        # 両方変数
        # 同じ変数ならOK
        if c1v == c2v:
            continue
        # 違う変数なら同値制約で結合
        uf.unite(c1v,c2v)

# 連結成分の変数リストを作成
for i in range(m):
    r = uf.find(i)
    group_vars.setdefault(r, []).append(i)

# 先頭文字、末尾文字の変数は0禁止制約のチェック
# 先頭文字が変数ならそのグループは0禁止
if arr[0][0] == 'v':
    r = uf.find(arr[0][1])
    group_zero_forbidden[r] = True
# (末尾が0禁止かは問題文のleading zeroの説明から不要と思われる)
# 片側のみ先頭が重要

# 各グループのuの範囲決定（複数変数のgroupの最小の範囲が有効）
for r,vs in group_vars.items():
    max_u = 99
    for v in vs:
        max_u = min(max_u, var_limits[vars_order[v]])
    group_vars[r] = (vs, max_u)

ans = 1
used_groups = set()
for r, (vs, max_u) in group_vars.items():
    if r in used_groups:
        continue
    used_groups.add(r)

    fixed_d = group_num_constraints.get(r, None)
    zero_forbid = group_zero_forbidden.get(r, False)

    if fixed_d is not None:
        # fixed_dがmax_uを超えていたら0通り
        if fixed_d > max_u:
            print(0)
            exit()
        # 0禁止＆値0のケースは0通り
        if zero_forbid and fixed_d == 0:
            print(0)
            exit()
        # これ1通りのみ
        ways = 1
    else:
        # 制約なし⇒0からmax_uまでの数字のうち、0禁止なら0省く
        ways = max_u +1
        if zero_forbid:
            ways -= 1
        if ways <= 0:
            print(0)
            exit()
    ans = (ans * ways) % MOD

print(ans)