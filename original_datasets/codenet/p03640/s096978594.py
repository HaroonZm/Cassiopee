h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = [[0 for j in range(w)] for i in range(h)]
nextColor = 0
H = 0
W = 0

while nextColor < n:
    # ai回マスを塗る
    for j in range(a[nextColor]):
        ans[H][W] = nextColor+1
        W += 1

        # 行末まで来たら次の行の先頭へ
        if W >= w:
            H += 1
            W = 0
    
    # 塗り終えたら次の色へ
    nextColor += 1

for i in range(h):
    # 奇数行は反転させる
    if i%2 != 0:
        ans[i] = ans[i][::-1]
    print(*ans[i])