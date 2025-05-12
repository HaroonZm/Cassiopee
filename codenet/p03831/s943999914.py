from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,a,b=map(int,readline().split())
    x=list(map(int,readline().split()))

    ans=0
    for i in range(n-1):
        if b<=a*(x[i+1]-x[i]):
            ans+=b
        else:
            ans+=a*(x[i+1]-x[i])
    
    print(ans)
    
if __name__=="__main__":
    main()