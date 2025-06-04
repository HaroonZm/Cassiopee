from functools import reduce
n_k = input().split(" ")
def to_ints(lst): return list(map(int, lst))
def compute_power(a, b, mod):
    result = 1
    for _ in range(b):
        result = (result * a) % mod
    return result
class MOD:
    def __init__(self,m): self.m = m
    def exp(self,base,exp): return pow(base,exp,self.m)
nums = to_ints(n_k)
if len(nums) == 2:
    n,k = nums
    m = 10**9+7
    modpow = MOD(m).exp if n%2==0 else (lambda a,b: compute_power(a,b,m))
    r = modpow(k,n)
    print((lambda x: x)(r))
else:
    print("Entrée invalide")