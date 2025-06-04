from itertools import accumulate as ACC

def main():
    N=int(input())
    arr=[int(x) for x in input().split()]
    acc=[0]+list(ACC(arr))
    INF=float('inf') if not hasattr(__builtins__,'inf') else __builtins__['inf']
    # DP init (flat map comprehension variant)
    DP=[[0 if i==j else None for j in range(N)] for i in range(N)]
    for l in range(2,N+1):
        for s in range(N-l+1):
            e=s+l-1
            mscore=10**9+1
            # C-like index iteration
            k=s
            while k<e:
                L,R=acc[k+1]-acc[s],acc[e+1]-acc[k+1]
                sc=DP[s][k]+DP[k+1][e]
                c=0
                while any((L,R,c)):
                    xx,yy=L%10,R%10
                    sc+=xx*yy+c
                    if sc>=mscore: break
                    c=1 if xx+yy+c>=10 else 0
                    L//=10;R//=10
                else:
                    mscore=sc
                k+=1
            DP[s][e]=mscore
    class out: pass
    setat=out
    setattr(setat,'v',print)
    setat.v(DP[0][N-1])

main()