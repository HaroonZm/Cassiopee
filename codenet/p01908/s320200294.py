N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)
    
class RollingHash:
    def __init__(self, s, base=1007, mod=10**9+7):
        self.s = s
        self.length = length = len(s)
        self.base = base
        self.mod = mod
        self.h = h = [0] * (length + 1)
        for i in range(length):
            h[i + 1] = (h[i] * base + ord(s[i])) % mod
        self.p = p = [1] * (length + 1)
        for i in range(length):
            p[i + 1] = pow(base, i + 1, mod)

    def get(self, l, r):
        mod = self.mod
        return ((self.h[r] - self.h[l] * self.p[r - l]) + mod) % mod
    
    
H = [RollingHash(s) for s in S]

abcd = [chr(97+i) for i in range(26)]
sub_strs = ['']
#print(abcd)
l = 1
while 1:
    sub_set = set()
    for h in H:
        for i in range(len(h.s)-(l-1)):
            sub_set.add(h.get(i,i+l))
    
    tmp = []
    for s1 in sub_strs:
        for s2 in abcd:
            tmp.append(s1+s2)
    sub_strs = tmp[:]
    
    flag = False
    for s in sub_strs:
        h = RollingHash(s).get(0,len(s))
        if h in sub_set:
            continue
        else:
            flag = s
            break
    if flag:
        print(s)
        break
    l += 1