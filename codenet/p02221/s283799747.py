import sys
readline = sys.stdin.readline

N = int(readline())
Ns = 1<<N
S = [None]+list(map(int, readline().strip()))
P = list(map(int, readline().split()))

res = [None]*Ns
res[0] = P
res[1] = P[1:] + [P[0]]
Ans = [None]*Ns

for i in range(Ns):
    ri = res[i]
    leng = len(ri)
    
    for level in range(leng.bit_length()-1):
        cnt = []
        for j in range(len(ri)//2):
            a = ri[2*j]
            b = ri[2*j+1]
            if S[abs(a-b)] == 1:
                cnt.append(max(a, b))
            else:
                cnt.append(min(a, b))
        ri = cnt[:]
        lri = len(ri)
        if 1 < Ns//lri < Ns-i:
            res[i + Ns//lri] = ri[1:] + [ri[0]]
    Ans[i] = ri[0]
print('\n'.join(map(str, Ans)))