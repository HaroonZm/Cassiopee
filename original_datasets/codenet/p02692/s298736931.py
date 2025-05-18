import sys
input = sys.stdin.readline

N,A,B,C=map(int,input().split())
S=[input().strip() for i in range(N)]

ANS=[]
for i in range(N):
    s=S[i]
    if s=="AB":
        if A==B==1 and i<N-1:
            if S[i+1]=="AC":
                A+=1
                B-=1
                ANS.append("A")
            else:
                B+=1
                A-=1
                ANS.append("B")

        else:
            if min(A,B)==A:
                A+=1
                B-=1
                ANS.append("A")
            else:
                B+=1
                A-=1
                ANS.append("B")

    elif s=="BC":
        if B==C==1 and i<N-1:
            if S[i+1]=="AC":
                C+=1
                B-=1
                ANS.append("C")
            else:
                B+=1
                C-=1
                ANS.append("B")

        else:
            if min(B,C)==B:
                B+=1
                C-=1
                ANS.append("B")
            else:
                C+=1
                B-=1
                ANS.append("C")

    else:
        if A==C==1 and i<N-1:
            if S[i+1]=="AB":
                A+=1
                C-=1
                ANS.append("A")
            else:
                C+=1
                A-=1
                ANS.append("C")

        else:
            if min(A,C)==A:
                A+=1
                C-=1
                ANS.append("A")
            else:
                C+=1
                A-=1
                ANS.append("C")

    if min(A,B,C)<0:
        print("No")
        sys.exit()

print("Yes")
print("\n".join(ANS))