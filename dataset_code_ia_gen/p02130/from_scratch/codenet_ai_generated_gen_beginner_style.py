N, A, B = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(N)]

used = [False] * N
count = 0

def check(diff):
    return abs(diff) <= A or (B <= abs(diff) <= 2 * A)

# まずは1要素ずつ削除できるものを処理
for i in range(N):
    if not used[i]:
        diff = pairs[i][0] - pairs[i][1]
        if check(diff):
            used[i] = True
            count += 1

# 次に2要素の組み合わせで削除できるものを処理
for i in range(N):
    if used[i]:
        continue
    for j in range(i+1, N):
        if used[j]:
            continue
        diff = (pairs[i][0] + pairs[j][0]) - (pairs[i][1] + pairs[j][1])
        if check(diff):
            used[i] = True
            used[j] = True
            count += 1
            break

print(count)