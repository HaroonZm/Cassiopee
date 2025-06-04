def main():
    getint=lambda: int(input())
    n=getint()
    a=[]
    for _ in range(n):a.append(getint())
    dp=[0]*n
    i=0
    while i<n:
        if i%2==n%2:
            def update_dp(dp):
                result=[]
                for l in range(n):
                    if a[l]>a[(l+i)%n]:
                        result.append(dp[(l+1)%n])
                    else:
                        result.append(dp[l])
                return result
            dp=update_dp(dp)
        else:
            dp = list(map(lambda l: max(a[l]+dp[(l+1)%n], a[(l+i)%n]+dp[l]), range(n)))
        i+=1
    print((lambda L: max(L))(dp))
main()