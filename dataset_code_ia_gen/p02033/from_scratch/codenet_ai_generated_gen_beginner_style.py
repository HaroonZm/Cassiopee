N,M = map(int, input().split())
m = list(map(int, input().split()))
Q = int(input())
l = list(map(int, input().split()))

# M個の送風機の位置をセットにする（位置は1からN）
blowers = set(m)

for allowed_loss in l:
    ans = -1
    # 矢の長さを1からNまで試す（初心者向け単純な解法）
    for length in range(1, N+1):
        loss = 0
        for x in range(1, N+1):
            # 先端がxにある時、矢の根元はx-lengthにある（根元位置はx-length）
            root_pos = x - length
            # 矢の区間は(root_pos, x]なので、経由する送風機の位置はmで、mは1~N
            # 矢の区間に少なくとも1つ送風機があれば損失にはならない
            # つまり、区間(root_pos, x]にblowerが含まれるかチェック
            # lengthは整数なので、区間内の送風機はm_iが x-length+1からx までか？
            # 送風機は位置 m_i で矢の先端から根元までに含まれるとは、x-length < m_i <= x
            exist = False
            for b in blowers:
                if root_pos < b <= x:
                    exist = True
                    break
            if not exist:
                loss += 1
            # 損失回数が許容を超えれば早期終了
            if loss > allowed_loss:
                break
        if loss <= allowed_loss:
            ans = length
            break
    print(ans)