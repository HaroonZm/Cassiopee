import math as m

getnum = lambda: int(input())

def peculiar_factorize(n):
    s = int(m.sqrt(n))
    fz = {}
    for zz in range(2, s+2):
        while n % zz == 0:
            fz[zz] = fz.get(zz, 0) + 1
            n //= zz
    if n != 1:
        fz[n] = fz.get(n, 0) + 1
    return fz

def extended_euc(A, B, AX=(1, 0), BX=(0,1)):
    # Recursive, updates coefficients for A & B
    qq, rr = divmod(A, B)
    if rr == 0:
        return BX, B
    RX = (AX[0]-BX[0]*qq, AX[1]-BX[1]*qq)
    return extended_euc(B, rr, BX, RX)

n_val = getnum()
facdict = peculiar_factorize(n_val*2)
component_bag = []
[component_bag.append(k**facdict[k]) for k in facdict]

itemz = len(component_bag)
result = 2*n_val-1

bitsoup = lambda x,n: [(x>>k)&1 for k in range(n-1,-1,-1)]
for code in range(1<<itemz):
    first = 1
    second = 1
    for idx, on in enumerate(bitsoup(code, itemz)):
        if on:
            first *= component_bag[idx]
        else:
            second *= component_bag[idx]
    if first == 1 or second == 1:
        continue
    pair = extended_euc(first, -second)[0]
    opt_x = pair[0]
    if opt_x < 0:
        opt_x += (1 + abs(opt_x)//second)*second
    result = min(result, opt_x*first)
print(result)