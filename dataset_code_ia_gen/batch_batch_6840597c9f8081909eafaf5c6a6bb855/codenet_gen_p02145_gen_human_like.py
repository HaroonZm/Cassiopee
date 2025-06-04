import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]

start_map = {}
for w in words:
    start_map.setdefault(w[0], []).append(w)

dp = {}
def dfs(last_char, used):
    key = (last_char, used)
    if key in dp:
        return dp[key]
    res = set()
    next_words = start_map.get(last_char, [])
    found = False
    for w in next_words:
        idx = word_idx[w]
        if (used >> idx) & 1 == 0:
            found = True
            res |= dfs(w[-1], used | (1 << idx))
    if not found:
        res.add(last_char)
    dp[key] = res
    return res

word_idx = {w:i for i,w in enumerate(words)}

result = set()
for i, w in enumerate(words):
    result |= dfs(w[-1], 1 << i)

for c in sorted(result):
    print(c)