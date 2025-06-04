from functools import reduce

def show_factors():
    n = int(input())
    res = list()
    i = 2
    while pow(i,2) <= n:
        if n % i: i += 1; continue
        while True:
            if n % i == 0:
                n = n // i
                res.append(i)
            else: break
        i += 1
    if n != 1: 
        res += [n]
    print(f"{n if not res else reduce(lambda x,y: x*y, res)}:", end=" ")
    for j in res: print(j, end=' ')
    
show_factors()