import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from bisect import bisect_left, bisect_right

N = int(readline())
m = map(int,read().split())
AB = zip(m,m)

graph = [[] for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)

root = 1
parent = [0] * (N+1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

def make_pairs(S,x):
    # a + b <= x となるペアをなるべくたくさん作る
    # nペア（なるべくたくさん）作ったあと、1つ短い長さが残る
    seg = 0
    while S and S[-1] == x:
        S.pop()
        seg += 1
    i = bisect_right(S,x//2)
    lower = S[:i][::-1]; upper = S[i:]
    cand = []
    rest = []
    for b in upper[::-1]:
        while lower and lower[-1] + b <= x:
            cand.append(lower.pop())
        if cand:
            cand.pop()
            seg += 1
        else:
            rest.append(b)
    cand += lower[::-1]
    L = len(cand)
    q,r = divmod(L,2)
    if r:
        return seg + len(rest) + q, cand[0]
    else:
        seg += q
        if rest:
            return seg + len(rest) - 1, rest[-1]
        else:
            # 全部ペアになった
            return seg, 0

def solve(x):
    # 長さ x までの線分を許容した場合に、必要となる本数を返す
    dp = [0] * (N+1)
    temp = [[] for _ in range(N+1)] # 下から出てくる長さ
    for v in order[::-1]:
        p = parent[v]
        S = temp[v]
        S.sort()
        s, l = make_pairs(S,x)
        dp[v] += s        
        dp[p] += dp[v]
        temp[p].append(l + 1)
        if v == 1:
            return dp[1] if not l else dp[1] + 1

seg = solve(N + 10)
left = 0 # むり
right = N # できる
while left + 1 < right:
    x = (left + right) // 2
    if solve(x) == seg:
        right = x
    else:
        left = x
print(seg, right)