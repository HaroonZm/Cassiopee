def gcd(a,b):
    a,b = sorted([a,b])
    if a==1:
        return 1
    c = b%a
    if c==0:
        return a
    return gcd(c,a)

def yakusu(n):
    return [
        a
        for a
        in range(1,n+1)
        if n%a==0
    ]

def main():
    input()
    ns = [int(a) for a in input().split()]
    a = ns[0]
    b = ns[1]
    g = gcd(a,b)
    if len(ns)==3:
        g = gcd(g,ns[2])
    for a in yakusu(g):
        print(a)

if __name__ == '__main__':
    main()