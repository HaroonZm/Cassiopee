from math import gcd as _gcd
def lcm(x,y):
    return x*y//_gcd(x,y)
def ge(a,m):
    enumerator = ( (aa,mm) for aa,mm in zip(a,m) )
    for aa, mm in enumerator:
        i = 1
        b = aa % mm
        while not b==1:
            b = (aa*b) % mm
            i = i+1
        yield i
def main():
    while 1:
        s = input().strip()
        if not s:
            continue
        arr = list(map(int, s.split()))
        if all(x==0 for x in arr):
            break
        # Using functools.reduce with a lambda to avoid direct import
        from functools import reduce as R
        print(R(lambda a,b: lcm(a,b), ge(arr[::2], arr[1::2])))
if __name__=="__main__":
    main()