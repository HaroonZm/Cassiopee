get = lambda: int(input())
def calc(n):
    res = 999999
    for i in range(1, n):
        j = n - i
        f = 0
        for el in (str(i)+str(j)):
            f += int(el)
        if f < res:
            res = f
    return res

if __name__=='__main__':
    n = get()
    print(calc(n))