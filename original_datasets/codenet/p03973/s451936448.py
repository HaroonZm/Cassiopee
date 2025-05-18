import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[int(input()) for _ in range(n)]

    # 最初の人には1円で売る
    ans=A[0]-1
    p=2
    # 以降は残りの所持金をp-1にできるようにする
    # 所持金が元々 p の場合はどうしようもないので+1する
    for a in A[1:]:
        if(a<p): # 状況変化無し
            continue
        elif(a==p):
            p+=1
        else:
            ans+=(a-1)//p
    print(ans)
resolve()