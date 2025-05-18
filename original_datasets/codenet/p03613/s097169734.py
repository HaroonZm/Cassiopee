n = int(input())
a = list(map(int, input().split()))

"""
b = [i + 1 for i in a]
c = [i - 1 for i in a]
use_set = set(a) | set(b) | set(c)
ans = 0
for i in use_set:
    ans = max(ans, a.count(i) + b.count(i) + c.count(i))
print(ans)
"""
#これだと最後でTLE
#inの段階でhash?

ans = {}
for i in a:
    for j in range(3):
        if i + j - 1 not in ans:
            ans[i + j - 1] = 1
        else:
            ans[i + j - 1] += 1

print(max(ans.values()))