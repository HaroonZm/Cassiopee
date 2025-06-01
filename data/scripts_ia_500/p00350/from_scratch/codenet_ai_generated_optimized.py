import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD1 = 10**9 + 7
MOD2 = 10**9 + 9
BASE1 = 911
BASE2 = 3571

class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.len = [0]*(2*self.size)
        self.hash1 = [0]*(2*self.size)
        self.hash2 = [0]*(2*self.size)
        self.lazy = [None]*(2*self.size)
        self.s = s

        # Precompute powers
        self.pow1 = [1]*(self.n+1)
        self.pow2 = [1]*(self.n+1)
        for i in range(self.n):
            self.pow1[i+1] = (self.pow1[i]*BASE1)%MOD1
            self.pow2[i+1] = (self.pow2[i]*BASE2)%MOD2

        for i in range(self.n):
            c = ord(s[i]) - ord('a') + 1
            self.len[self.size+i] = 1
            self.hash1[self.size+i] = c
            self.hash2[self.size+i] = c
        for i in range(self.size-1,0,-1):
            self.len[i] = self.len[i<<1] + self.len[i<<1|1]
            self.hash1[i] = (self.hash1[i<<1]*self.pow1[self.len[i<<1|1]] + self.hash1[i<<1|1])%MOD1
            self.hash2[i] = (self.hash2[i<<1]*self.pow2[self.len[i<<1|1]] + self.hash2[i<<1|1])%MOD2

    def _apply(self, i, c):
        length = self.len[i]
        val = ord(c) - ord('a') + 1
        self.hash1[i] = val * (self.pow1[length] - 1) * pow(BASE1-1, MOD1-2, MOD1) % MOD1
        self.hash2[i] = val * (self.pow2[length] - 1) * pow(BASE2-1, MOD2-2, MOD2) % MOD2
        self.lazy[i] = c

    def _push(self, i):
        if self.lazy[i] is not None:
            self._apply(i<<1, self.lazy[i])
            self._apply(i<<1|1, self.lazy[i])
            self.lazy[i] = None

    def _update(self, i):
        self.hash1[i] = (self.hash1[i<<1]*self.pow1[self.len[i<<1|1]] + self.hash1[i<<1|1])%MOD1
        self.hash2[i] = (self.hash2[i<<1]*self.pow2[self.len[i<<1|1]] + self.hash2[i<<1|1])%MOD2

    def update(self,l,r,c,i=1,left=0,right=None):
        if right is None:
            right = self.size
        if r<=left or right<=l:
            return
        if l<=left and right<=r:
            self._apply(i,c)
            return
        self._push(i)
        mid = (left+right)>>1
        self.update(l,r,c,i<<1,left,mid)
        self.update(l,r,c,i<<1|1,mid,right)
        self._update(i)

    def query(self,l,r,i=1,left=0,right=None):
        if right is None:
            right = self.size
        if r<=left or right<=l:
            return (0,0,0)
        if l<=left and right<=r:
            return (self.hash1[i], self.hash2[i], self.len[i])
        self._push(i)
        mid = (left+right)>>1
        h1_l, h2_l, len_l = self.query(l,r,i<<1,left,mid)
        h1_r, h2_r, len_r = self.query(l,r,i<<1|1,mid,right)
        h1 = (h1_l*self.pow1[len_r] + h1_r)%MOD1
        h2 = (h2_l*self.pow2[len_r] + h2_r)%MOD2
        return (h1,h2,len_l+len_r)

def main():
    N = int(input())
    U = input().rstrip('\n')
    Q = int(input())
    seg = SegmentTree(U)

    for _ in range(Q):
        query = input().split()
        if query[0] == 'set':
            x,y,z = query[1],query[2],query[3]
            x = int(x)-1
            y = int(y)
            seg.update(x,y,z)
        else:
            a,b,c,d = map(int,query[1:])
            a-=1
            b-=1
            c-=1
            d-=1
            len1 = b - a + 1
            len2 = d - c + 1
            length = min(len1,len2)

            # Binary search for first differing char
            low = 0
            high = length+1
            while low < high:
                mid = (low + high)//2
                h1 = seg.query(a,a+mid)
                h2 = seg.query(c,c+mid)
                if h1[0] == h2[0] and h1[1] == h2[1]:
                    low = mid+1
                else:
                    high = mid
            pos = low - 1
            if pos == length:
                # all equal, compare length
                if len1 == len2:
                    print('e')
                elif len1 < len2:
                    print('s')
                else:
                    print('t')
            else:
                ch1 = seg.query(a+pos,a+pos+1)
                ch2 = seg.query(c+pos,c+pos+1)
                if ch1[0] < ch2[0]:
                    print('s')
                elif ch1[0] > ch2[0]:
                    print('t')
                else:
                    print('e')

if __name__ == "__main__":
    main()