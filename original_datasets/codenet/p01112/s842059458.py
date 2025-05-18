from collections import defaultdict
def main(n):
    m = int(input())
    d = defaultdict(int)
    k = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            d[k] = (i, j)
            k += 1
    p = defaultdict(int)
    for i in range(m):
        x, y = map(int, input().split())
        p[(x, y)] = 1
        p[(y, x)] = -1
    ans = defaultdict(int)
    tmp = [0] * n
    ans[tuple(tmp)] = 1
    for i in range(k):
        nd = defaultdict(int)
        for key, value in ans.items():
            key = list(key)
            x, y = d[i]
            if p[(x, y)]:
                if p[(x, y)] == 1:
                    if key[x - 1] == n//2: continue
                    key[x - 1] += 1
                    nd[tuple(key)] += value
                else:
                    if key[y - 1] == n//2: continue
                    key[y - 1] += 1
                    nd[tuple(key)] += value
            else:
                    if key[y - 1] != n//2: 
                        key[y - 1] += 1
                        nd[tuple(key)] += value
                        key[y - 1] += -1
                    if key[x - 1] != n//2:
                        key[x - 1] += 1
                        nd[tuple(key)] += value
        ans = nd
    print(ans[tuple([n // 2] * n)])

if __name__ == "__main__":
    while 1:
        n = int(input())
        if n:
            main(n)
        else:
            break