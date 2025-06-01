from bisect import bisect_right as br
from itertools import accumulate

def main():
    m, n = map(int, input().split())
    books = [list(map(int, input().split())) for _ in range(m)]
    ws = list(accumulate([0] + [book[0] for book in books]))
    ts = list(accumulate([0] + [book[1] for book in books]))
    shelf = [list(map(int, input().split())) for _ in range(n)]
    dic = {}
    rest = 2 ** n - 1
    def search(index, num):
        wlim, tlim = shelf[num]
        wind = br(ws, ws[index] + wlim)
        tind = br(ts, ts[index] + tlim)
        return min(wind, tind) - 1
    def dp(rest, dic):
        if rest in dic:
            return dic[rest]
        if rest == 0:
            return 0
        mask = 1  
        ret = 0
        for i in range(n):
            if rest & mask:
                pre_rest = rest & ~mask
                temp = dp(pre_rest, dic)
                temp = search(temp, i)
                ret = max(ret, temp)
            mask <<= 1
        dic[rest] = ret
        return ret
    print(dp(rest, dic))

main()