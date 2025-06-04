from functools import lru_cache
from itertools import product, chain, repeat

def main():
    n = int(input())
    lst = [(*s.split()[0], int(s.split()[1])) for s in (input() for _ in range(n))]
    mp = ["#"*6] + ["#" + input() + "#" for _ in range(4)] + ["#"*6]
    t = int(input())

    vec = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    @lru_cache(maxsize=None)
    def search(word):
        def pos_gen(ch):
            return ((x, y) for y, x in product(range(1,5), repeat=2) if mp[y][x]==ch)
        
        @lru_cache(maxsize=None)
        def dfs(idx, x, y, used_mask):
            if idx == len(word) - 1:
                return 1
            res = 0
            for dx, dy in vec:
                nx, ny = x+dx, y+dy
                pos = (ny-1)*4 + (nx-1)
                if 1<=nx<=4 and 1<=ny<=4 and not (used_mask & (1<<pos)) and mp[ny][nx]==word[idx+1]:
                    res += dfs(idx+1, nx, ny, used_mask | (1<<pos))
            return res

        total = 0
        for x, y in pos_gen(word[0]):
            pos = (y-1)*4 + (x-1)
            total += dfs(0, x, y, 1<<(pos))
        return total

    items = []
    for raw_word, score in lst:
        word = ''.join(raw_word)
        cnt = search(word)
        acc, weight = 1, len(word)
        while cnt >= acc:
            cnt -= acc
            items.append((score * acc, weight * acc))
            acc <<= 1
        if cnt:
            items.append((score * cnt, weight * cnt))

    dp = [0]*(t+1)
    for v, w in items:
        for x in range(t, w-1, -1):
            if dp[x] < dp[x-w]+v:
                dp[x] = dp[x-w]+v
    print(max(dp))

main()