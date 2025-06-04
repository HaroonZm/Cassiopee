import sys
import math

def main():
    input=sys.stdin.readline
    N,M=map(int,input().split())
    vectors=[list(map(float,input().split())) for _ in range(M)]

    # Precompute dot products
    dot=[[0]*M for _ in range(M)]
    for i in range(M):
        vi=vectors[i]
        for j in range(i,M):
            vj=vectors[j]
            s=0
            for k in range(N):
                s+=vi[k]*vj[k]
            dot[i][j]=s
            dot[j][i]=s

    dp=[0]*M
    for i in range(M):
        # cost if record as is
        len_vi=dot[i][i]
        best=len_vi
        for j in range(i):
            vj_vj=dot[j][j]
            if vj_vj==0:
                continue
            vij=dot[i][j]
            r=vij/vj_vj
            # squared length of (v_i - r v_j)
            val=dot[i][i]-r*r*vj_vj*2+ r*r*vj_vj
            # Simplify: (v_i - r v_j)^2 = v_i.v_i - 2r v_i.v_j + r^2 v_j.v_j
            val=dot[i][i]-2*r*vij + r*r*vj_vj
            # total cost if predecessor j plus this diff vector
            cost=dp[j]+val
            if cost<best:
                best=cost
        dp[i]=best
    print(f"{dp[M-1]:.9f}")

if __name__=="__main__":
    main()