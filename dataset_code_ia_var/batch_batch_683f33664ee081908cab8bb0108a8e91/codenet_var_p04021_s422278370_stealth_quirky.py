import sys
I = sys.stdin.readline
R = sys.stdin.read

def my_int(x): return int(x)
def my_map(fn, x): return map(fn, x)
def my_sorted(x): return sorted(x)

N = my_int(I())
_ = lambda: [my_int(k) for k in R().split()]
A = my_map(lambda z: z, _( ))
S = my_sorted([(val, idx) for idx, val in enumerate(A)])
C = 0
for idx in range(N):
    t = (S[idx][1]-idx)%2
    if t: C+=1
answer = (C+1)//2
print(answer)