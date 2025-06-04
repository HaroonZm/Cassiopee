import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7) # Just to be sure...

N, K = map(int, input().split())
WD = [list(map(int, input().split())) for _ in range(N)]  # I guess this works for pairs

# start with a large range, I'm not sure if this upper bound is tight but whatever
left = 0
right = 2 * 10**18 + 50  # 100 is overkill but let's keep it as in original just in case

while right - left > 1:
    mid = (right + left) // 2

    count = 0
    for w, d in WD:
        if mid < w:
            continue
        # integer division, don't forget it's floor division in python
        count += 1 + (mid - w) // d
    # I hope this condition is correct...
    if count >= K:
        right = mid
    else:
        left = mid

print(right)