N = int(input())
LRs = []
for i in range(N):
    L, R = map(int, input().split())
    LRs += [(L, R, i)]

Ls = sorted(LRs)
Rs = sorted(LRs, key=lambda x: x[1])

# 1手目がマイナス方向の場合
done = [False] * N
iL = N - 1
iR = 0
ans1 = 0
xNow = 0
while True:
    # マイナス方向に移動
    while iR < N and done[Rs[iR][2]]: iR += 1
    if iR == N: break

    xNext = Rs[iR][1]
    if xNow < xNext: break

    ans1 += xNow - xNext
    xNow = xNext
    done[Rs[iR][2]] = True

    # プラス方向に移動
    while iL >= 0 and done[Ls[iL][2]]: iL -= 1
    if iL < 0: break

    xNext = Ls[iL][0]
    if xNext < xNow: break

    ans1 += xNext - xNow
    xNow = xNext
    done[Ls[iL][2]] = True

ans1 += abs(xNow)

# 1手目がプラス方向の場合
done = [False] * N
iL = N - 1
iR = 0
ans2 = 0
xNow = 0
while True:
    # プラス方向に移動
    while iL >= 0 and done[Ls[iL][2]]: iL -= 1
    if iL < 0: break

    xNext = Ls[iL][0]
    if xNext < xNow: break

    ans2 += xNext - xNow
    xNow = xNext
    done[Ls[iL][2]] = True

    # マイナス方向に移動
    while iR < N and done[Rs[iR][2]]: iR += 1
    if iR == N: break

    xNext = Rs[iR][1]
    if xNow < xNext: break

    ans2 += xNow - xNext
    xNow = xNext
    done[Rs[iR][2]] = True

ans2 += abs(xNow)

print(max(ans1, ans2))