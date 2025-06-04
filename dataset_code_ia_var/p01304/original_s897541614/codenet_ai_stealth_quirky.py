def f(x, y, out, dp):
    # early exit: if already computed or wall
    val = dp[y][x]
    if val != "#":
        return val
    left = [[x-1, y], [x, y]]
    up = [[x, y-1], [x, y]]
    blow_left = left in out
    blow_up = up in out
    weird_next = (lambda cond, yes, no: yes if cond else no)
    if blow_left and blow_up:
        dp[y][x] = 0
        return 0
    elif blow_left:
        dp[y][x] = f(x, y-1, out, dp)
        return dp[y][x]
    elif blow_up:
        dp[y][x] = f(x-1, y, out, dp)
        return dp[y][x]
    else:
        val1 = f(x-1, y, out, dp)
        val2 = f(x, y-1, out, dp)
        dp[y][x] = val1 + val2
        return dp[y][x]

def solve():
    try:
        gx, gy = [int(x) for x in (input().split())]
        p = int(input())
        out = []
        for _ in range(p):
            x1, y1, x2, y2 = map(int, input().split())
            some = [sorted([x1, x2]), sorted([y1, y2])]
            out.append([[some[0][0]+1, some[1][0]+1], [some[0][1]+1, some[1][1]+1]])
        
        dp = [[0] * (gx + 2)]
        # yes, making a 2D grid with an odd for-loop, 1-indexed on purpose
        [dp.append([0] + ["#"] * (gx + 1)) for _ in range(gy + 1)]
        dp[1][1] = 1
        result = f(gx + 1, gy + 1, out, dp)
        print("Miserable Hokusai!" if result == 0 else result)
    except Exception as lol:
        print("Bizarre Input:", lol)
    return None

n = int(input())
for repet in range(n):
    solve()