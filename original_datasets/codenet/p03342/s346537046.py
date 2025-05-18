# Your code here!
n=int(input())
A=list(map(int,input().split()))
ans=0
l=0;r=0
nowsum =0#ここでf(0,0)を計算
nowxsum=0
for l in range(0,n):
    while(r < n and (nowsum + A[r] == nowxsum ^ A[r])):#f(l,r+1)が条件をみたすかチェック
        nowsum  += A[r] #ここでf(l,r+1)にうつる
        nowxsum ^= A[r]
        r +=1
    #f(l,r) < Sとなる最大のrがとれた！
    ans += r-l #ここで問題に必要な値を計算
    nowsum -= A[l] #ここでf(l+1,r)を計算
    nowxsum ^= A[l] #ここでf(l+1,r)を計算
print(ans)