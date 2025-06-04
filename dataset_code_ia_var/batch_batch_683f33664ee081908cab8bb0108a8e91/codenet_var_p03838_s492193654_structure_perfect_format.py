x, y = map(int, input().split())
ans = float('inf')

# 0,0
if y - x > 0:
    ans = min(ans, y - x)

# 1,0
if -x <= y:
    ans = min(ans, 1 + y + x)

# 0,1
if x <= -y:
    ans = min(ans, 1 - y - x)

# 1,1
if -x <= -y:
    ans = min(ans, 2 - y + x)

print(ans)