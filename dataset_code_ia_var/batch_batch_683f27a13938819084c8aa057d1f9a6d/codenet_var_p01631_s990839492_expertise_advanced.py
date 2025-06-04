from sys import stdin
from functools import lru_cache
from itertools import product, chain

def main():
    n = int(stdin.readline())
    words_scores = [stdin.readline().split() for _ in range(n)]
    words, scores = zip(*((w, int(s)) for w, s in words_scores))
    mp = (
        ["#" * 6] +
        ["#" + stdin.readline().strip() + "#" for _ in range(4)] +
        ["#" * 6]
    )
    t = int(stdin.readline())

    DIRS = tuple(product((-1, 0, 1), repeat=2))
    DIRS = tuple((dx, dy) for dx, dy in DIRS if dx or dy)
    
    @lru_cache(maxsize=None)
    def valid_pos(x, y):
        return 0 < x < 5 and 0 < y < 5

    def search(word):
        word_len = len(word)
        used = [[False]*6 for _ in range(6)]

        @lru_cache(maxsize=None)
        def _search(pos, x, y):
            if pos == word_len - 1:
                return 1
            used[y][x] = True
            total = 0
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if valid_pos(nx, ny) and not used[ny][nx] and mp[ny][nx] == word[pos+1]:
                    total += _search(pos + 1, nx, ny)
            used[y][x] = False
            return total

        starts = [
            (x, y)
            for y, x in product(range(1, 5), repeat=2)
            if mp[y][x] == word[0]
        ]
        count = 0
        for x, y in starts:
            count += _search(0, x, y)
        _search.cache_clear()
        return count

    items = []
    for word, score in zip(words, scores):
        cnt = search(word)
        acc = 1
        while cnt >= acc:
            items.append((len(word)*acc, score*acc))
            cnt -= acc
            acc <<= 1
        if cnt:
            items.append((len(word)*cnt, score*cnt))

    dp = [0] * (t + 1)
    for w, v in items:
        for j in range(t, w-1, -1):
            dp[j] = max(dp[j], dp[j-w] + v)
    print(max(dp))

main()