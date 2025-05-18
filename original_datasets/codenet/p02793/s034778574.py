from fractions import gcd
def main():
    N=int(input())
    A=list(map(int,input().split()))
    mod=10**9+7
    b=0
    c=1
    for a in A:
        c=c*a//gcd(c,a)
    c%=mod
    for a in A:
        b+=c*pow(a,mod-2,mod)
    print(b%mod)
if __name__=="__main__":
    main()