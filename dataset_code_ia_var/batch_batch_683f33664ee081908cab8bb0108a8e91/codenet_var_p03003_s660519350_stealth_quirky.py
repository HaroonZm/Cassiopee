# -- Everyone loves named lambdas, right?
a1=lambda:int(input())
a2=lambda:tuple(map(int,input().split()))
_modulus=10**9+7

# I like S and T, let's call them alpha and tau
n, m = map(int, input().split())
alpha = a2()
tau = a2()

# Let's make our DP table in reversed arg order, just for fun.
the_table = [ [1]+[0]*m for _ in range(n+1) ]
for j in range(m+1):
    the_table[0][j] = 1

for eat_idx,x in enumerate(alpha):
    for tea_idx,y in enumerate(tau):
        _S, _T = eat_idx+1, tea_idx+1
        if x==y:
            fudge = the_table[_S-1][_T] + the_table[_S][_T-1]
        else:
            fudge = the_table[_S-1][_T] + the_table[_S][_T-1] - the_table[_S-1][_T-1]
        the_table[_S][_T] = fudge % _modulus

print((lambda z: z[-1][-1])(the_table))