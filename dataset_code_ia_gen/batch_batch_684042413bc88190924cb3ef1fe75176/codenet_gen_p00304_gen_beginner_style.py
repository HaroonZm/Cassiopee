import sys
sys.setrecursionlimit(10**7)

MOD = 1000000007

N = int(input())
nodes = []
for _ in range(N):
    nodes.append(input())

children = [[] for _ in range(N)]
for _ in range(N-1):
    s, t = map(int, input().split())
    children[s-1].append(t-1)

# ノードの種類判定用関数
def is_option(s):
    return s.endswith('?')

def is_substance(s):
    # E, E?が物質ノード
    return s.startswith('E')

def is_select(s):
    # A, A?, R, R?が選択ノード
    return s[0] == 'A' or s[0] == 'R'

def type_of_node(s):
    # 物質: 'E'
    # 選択ノード: 'A'または'R'
    return s[0]

# メイン処理: ノードiでの組み合わせ数を返す
def dfs(i):
    node = nodes[i]
    opt = is_option(node)
    if is_substance(node):
        # 物質ノード
        # オプションでないなら必ず選ぶ → 組み合わせ数は子ノードの組み合わせ数の積
        # オプションなら選ぶか選ばないか → (1 + 子ノードの組み合わせ数の積)
        # 子はいない可能性があるが、あるなら計算

        # 子ノードは必ずオプションでないので普通に計算
        val = 1
        for c in children[i]:
            val = (val * dfs(c)) % MOD

        if opt:
            # オプション物質ノードは選ぶか選ばないか
            val = (val + 1) % MOD
        # オプションでない物質は必ず選ぶ → valのまま
        return val
    else:
        # 選択ノード
        # 子ノードはオプションでない物質ノードのみ
        # 2種類の型がある
        typ = type_of_node(node)

        # 子ノードの組み合わせ数を計算する
        child_vals = []
        for c in children[i]:
            child_vals.append(dfs(c))

        if typ == 'R':
            # or型: 子から少なくとも一つ選ぶ (オプションなら0個もOK)
            # 組み合わせは (∏(1+子の組み合わせ)) - 1 (少なくとも一つ選ぶ)
            # オプションなら -1しない(0個もOK)
            mul = 1
            for v in child_vals:
                mul = (mul * (v + 1)) % MOD
            if opt:
                # オプションの or型は0個選んでもよいのでそのまま
                return mul % MOD
            else:
                # オプションでない or型は少なくとも一つ選ぶので-1
                return (mul - 1) % MOD

        else:
            # alt型: 子から一つだけ選ぶ (オプションなら0個選んでもよい)
            summ = 0
            for v in child_vals:
                summ = (summ + v) % MOD
            if opt:
                # オプションの altは0個もOK → (sum + 1)
                return (summ + 1) % MOD
            else:
                # オプションでない altは必ず一つ選ぶ → sum
                return summ % MOD

res = dfs(0)
print(res % MOD)