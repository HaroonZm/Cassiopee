N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

def func(x):
    attack = 0
    for h in H:
        hp = h - B * x
        if hp <= 0:
            continue
        attack += -(-hp // (A - B))
        # B*Xで足りない分対象に選んでAで補填するが、対象に選ぶということは
        # 選んだ数n分Bがなくなるということ。hp=h-B*(x-n)
        # 対象nの分(A-B)増加と言い換えられ、対象回数はhp//(A-B)の繰り上げで求まる。
    if attack > x:
        return 0
    else:
        return 1

l, r = -1, 10 ** 9
while (r - l > 1):
    mid = (l + r) // 2
    if func(mid):
        r = mid
    else:
        l = mid

print(r)