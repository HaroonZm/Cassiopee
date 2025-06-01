import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, K = map(int, input().split())

# Union-Find構造
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

def same(a, b):
    return find(a) == find(b)

# 部活動所属の管理用配列
# 部活動を示す値が 0 の場合未所属
club_of = [0] * (N + 1)

ans = 0
for i in range(1, K + 1):
    record = list(map(int, input().split()))
    t = record[0]
    if t == 1:
        a, b = record[1], record[2]
        # a, bが所属する部活動が異なって矛盾がないか確認
        # 両方が部活加入済みで所属部活が違う -> 矛盾
        if club_of[a] != 0 and club_of[b] != 0 and club_of[a] != club_of[b]:
            ans = i
            break
        # そうでなければa,bを併合
        unite(a, b)
        # 部活情報を併合後に更新する
        ra = find(a)
        # raの部活に何か入っているか
        ca = club_of[ra] if ra <= N else 0
        # 両方の部活情報のうち0でないならそれにする
        if club_of[a] != 0:
            club_of[ra] = club_of[a]
        if club_of[b] != 0:
            club_of[ra] = club_of[b]
        # a,bともに部活動が0のときは何もしない

    else:
        c, x = record[1], record[2]
        rc = find(c)
        # cの部活が0かつrcの部活が0なら所属設定
        # 既に別の部活所属なら矛盾
        if club_of[rc] != 0 and club_of[rc] != x:
            ans = i
            break
        club_of[rc] = x

print(ans) if ans else print(0)