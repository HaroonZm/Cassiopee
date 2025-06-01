import sys
sys.setrecursionlimit(10**7)

def dfs(i):
    p, q, r, b = sticks[i]
    # 赤端につるす先の重さ
    if r == 0:
        red_w = 1
    else:
        red_w = dfs(r-1)
    # 青端につるす先の重さ
    if b == 0:
        blue_w = 1
    else:
        blue_w = dfs(b-1)
    # バランス式よりこの棒の重さを計算
    w = red_w * p + blue_w * q
    return w

input_lines = sys.stdin.read().splitlines()
idx = 0
while True:
    if idx >= len(input_lines):
        break
    n = int(input_lines[idx].strip())
    idx += 1
    if n == 0:
        break
    sticks = []
    for _ in range(n):
        p,q,r,b = map(int, input_lines[idx].split())
        idx += 1
        sticks.append((p,q,r,b))
    ans = dfs(0)
    print(ans)