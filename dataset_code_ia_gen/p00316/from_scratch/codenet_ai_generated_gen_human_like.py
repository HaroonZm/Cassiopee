import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, K = map(int, input().split())

# Union-Find (Disjoint Set Union)実装
parent = list(range(N+1))
rank = [0] * (N+1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x, y):
    return find(x) == find(y)

# 生徒と部活動の所属を管理する
# 部活は1~M、生徒は1~N
# 部活xに所属する生徒の代表を記録　key: 部活番号, value: 生徒の親（代表）
club_rep = dict()
# 生徒が所属している部活（0なら未所属）
student_club = [0]*(N+1)

ans = 0

for i in range(1, K+1):
    t, a, b = map(int, input().split())
    if t == 1:
        # a,bは同じ部活
        # 矛盾：a,bが既に別の部活所属の生徒同士で同じ部活に出来ない時は矛盾
        root_a = find(a)
        root_b = find(b)
        # aの所属部活があれば、それの代表も入手、なければ0
        club_a = student_club[root_a]
        club_b = student_club[root_b]
        if root_a == root_b:
            # すでに同じグループなので矛盾なし
            continue
        # 両方の部活が存在していて違うなら矛盾
        if club_a != 0 and club_b != 0 and club_a != club_b:
            ans = i
            break
        # 問題なければ併合して、部活情報の更新をする
        unite(root_a, root_b)
        new_root = find(root_a)
        # 部活の情報を設定
        if club_a != 0 and club_b == 0:
            student_club[new_root] = club_a
        elif club_b != 0 and club_a == 0:
            student_club[new_root] = club_b
        elif club_a == 0 and club_b == 0:
            student_club[new_root] = 0
        else:
            # 両方0は上で排除されているが念のため
            student_club[new_root] = club_a
    else:
        # aは部活bに所属
        root_a = find(a)
        club_a = student_club[root_a]
        # すでに所属している部活が違う場合は矛盾
        if club_a != 0 and club_a != b:
            ans = i
            break
        # 所属部活を登録
        student_club[root_a] = b

print(ans)