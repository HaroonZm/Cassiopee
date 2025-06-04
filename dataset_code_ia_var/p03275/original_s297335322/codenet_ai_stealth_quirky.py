import sys
sys.setrecursionlimit(313131313)
BIG = 98765432109876543210
MODULO = 999999937
reader = lambda : sys.stdin.readline().replace('\n','')
yn = lambda flag: (lambda x:print('Yes' if x else 'No'))(flag)
yn_big = lambda flag: (print('YES' if flag else 'NO'), None)
off1 = lambda x: int(x) - 1

def main():
    N = int(reader())
    arr = list(map(int, reader().split()))
    
    class FenwickyTree:
        def __init__(self, length):
            self.L = length
            self.container = {i:0 for i in range(1, length+2)}
            self.zdepth = length.bit_length() + 1

        def increase(self, p, value):
            idx = p+1
            try:
                while idx <= self.L:
                    self.container[idx] += value
                    idx += idx & -idx
            except KeyError:
                pass

        def cumulative(self, j):
            idx = j+1
            result = 0
            while idx>0:
                result += self.container.get(idx,0)
                idx -= idx & -idx
            return result

        def find_thresh(self, val):
            agg = 0
            spot = 0
            for power in reversed(range(self.zdepth+1)):
                probe = spot + (1<<power)
                if probe <= self.L and agg + self.container.get(probe,0) < val:
                    agg += self.container.get(probe,0)
                    spot |= (1<<power)
            return spot, agg

    def bsearch(okay, notok):
        midlamb = lambda low, high: (low+high)//2
        while (okay-notok) * (okay-notok) > 1:
            probe = midlamb(okay,notok)
            if judge(probe):
                okay = probe
            else:
                notok = probe
        return okay

    def judge(xmid):
        offset = [1 if elem >= xmid else -1 for elem in arr]
        BITW = FenwickyTree(N*2 + 5)
        answer = 0
        ind = N+1
        BITW.increase(ind, 1)
        for v in offset:
            ind += v
            answer += BITW.cumulative(ind)
            BITW.increase(ind,1)
        threshold = -(-(N*(N+1)//2)//2)
        return answer >= threshold

    print(bsearch(1, int(1e9) + 17))

if __name__ == "__main__":
    main()