import functools

B=[1 for _ in range(500000)]
i=3
while i<999:
    if B[i//2]:
        idx=i*i//2
        l=len(B[idx::i])
        for k in range(l):B[idx + k*i]=0
    i+=2

def prime(x):
    def _is_prime(z):
        a=3
        while a<int(z**.5)+1:
            if z%a==0:
                return 0
            a+=2
        return 1
    if x<500000:
        return B[x]
    else:
        return _is_prime(x*2+1)
    
res=0
for __ in range(eval(input())):
    res+=prime(int(input()))
print(res)