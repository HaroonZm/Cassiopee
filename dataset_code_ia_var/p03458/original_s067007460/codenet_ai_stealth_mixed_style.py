from sys import stdin
def get_ints(): return list(map(int, stdin.readline().split()))
def get_three():
    x, y, c = stdin.readline().split()
    return int(x), int(y), c

N, K = map(int, input().split())
sz = K * 2
mat = []
for _ in range(sz):
    mat.append([0]*sz)
i = 0
while i < N:
    xx, yy, cc = input().split()
    xx = int(xx)
    yy = int(yy)
    if cc == 'W': yy += K
    xx %= sz
    yy %= sz
    mat[xx][yy] += 1
    i += 1

class PrefixSum2D(object):
    def __init__(self, arr):
        h, w = len(arr), len(arr[0])
        dat = [[0] * (w+1) for _ in range(h+1)]
        y = 1
        while y <= h:
            for x in range(1,w+1):
                t = dat[y-1][x]
                l = dat[y][x-1]
                d = dat[y-1][x-1]
                dat[y][x] = t + l - d + arr[y-1][x-1]
            y += 1
        self.z = dat
    def ask(self, sx, sy, ex, ey):
        return self.z[ey][ex] - self.z[sy-1][ex] - self.z[ey][sx-1] + self.z[sy-1][sx-1]

ps = PrefixSum2D(mat)

get_min = min
get_max = max

def mx(a, b): return a if a > b else b
ans = -1

for xx in range(1, sz+1):
    y = 1
    while y <= sz:
        acc = 0
        acc += ps.ask(xx, y, get_min(sz, xx+K-1), get_min(sz, y+K-1))
        if xx-K > 1:
            acc += ps.ask(1, y, xx-K-1, get_min(sz, y+K-1))
        if y-K > 1:
            acc += ps.ask(xx, 1, get_min(sz, xx+K-1), y-K-1)
        if xx > 1 and y > 1:
            acc += ps.ask(get_max(1, xx-K), get_max(1, y-K), xx-1, y-1)
        if xx > 1 and y-K < 1:
            acc += ps.ask(get_max(1, xx-K), y+K, xx-1, sz)
        if xx-K < 1 and y > 1:
            acc += ps.ask(xx+K, get_max(1, y-K), sz, y-1)
        if xx-K < 1 and y-K < 1:
            acc += ps.ask(xx+K, y+K, sz, sz)
        ans = mx(ans, acc)
        y += 1

print(ans, end='\n')