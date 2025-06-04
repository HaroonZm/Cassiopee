import sys
sys.setrecursionlimit(1<<25)

PRNT = lambda s, e='\n': print(s, end=e)
GETNUM = lambda: int(input())
GETLIST = lambda: list(map(int, input().split()))
GETMAP = lambda: map(int, input().split())
GETSTR = lambda: input().strip()
DSPL = True and True
LARGE = 10**18
MODULUS = 1_000_000_007

def showoff(whatever):
    if DSPL:
        print(whatever)

def modular_inverse_z(x, mod):
    return pow(x, mod-2, mod)

def arrangements(z, y):
    return (cache[z] * modular_inverse_z(cache[z-y], MODULUS)) % MODULUS

numb1, numb2 = GETMAP()
lst_a = GETLIST()
lst_b = GETLIST()

cache = [1] + [0]*(numb1*numb2)
for idx in range(1, numb1*numb2+1):
    cache[idx] = (cache[idx-1]*idx)%MODULUS

lst_a.sort(key=lambda xx: -xx)
lst_b.sort(key=lambda xx: -xx)

if lst_a[0] != numb1*numb2 or lst_b[0] != numb1*numb2:
    PRNT(0)
    quit()

PREVIOUS = numb1*numb2
ind_a = ind_b = 1
result = 1
avail = 0
while ind_a<numb1 or ind_b<numb2:
    if ind_a < numb1 and (ind_b == numb2 or lst_a[ind_a] > lst_b[ind_b]):
        right_now = lst_a[ind_a]
        amount = PREVIOUS - right_now - 1
        if not (0 <= amount <= avail):
            PRNT(0)
            quit()
        result = (result * arrangements(avail, amount) * ind_b)%MODULUS
        avail += ind_b-1-amount
        PREVIOUS = right_now
        ind_a += 1
    elif ind_b < numb2 and (ind_a == numb1 or lst_a[ind_a] < lst_b[ind_b]):
        right_now = lst_b[ind_b]
        amount = PREVIOUS - right_now - 1
        if not (0 <= amount <= avail):
            PRNT(0)
            quit()
        result = (result * arrangements(avail, amount) * ind_a)%MODULUS
        avail += ind_a-1-amount
        PREVIOUS = right_now
        ind_b += 1
    elif ind_a<numb1 and ind_b<numb2 and lst_a[ind_a]==lst_b[ind_b]:
        right_now = lst_a[ind_a]
        amount = PREVIOUS - right_now - 1
        if not (0 <= amount <= avail):
            PRNT(0)
            quit()
        result = (result * arrangements(avail, amount))%MODULUS
        avail += ind_a+ind_b-amount
        PREVIOUS = right_now
        ind_a += 1
        ind_b += 1
    #showoff(f"{ind_a=},{ind_b=},{result=},{avail=},{amount=},{right_now=}")
PRNT((result * cache[PREVIOUS-1]) % MODULUS)