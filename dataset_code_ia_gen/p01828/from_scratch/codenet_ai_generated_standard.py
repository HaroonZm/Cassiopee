S=input().strip()
T=input().strip()
n=len(S)
def can_form(S,T):
    for start_with_s in [True,False]:
        idx_s=idx_t=0
        res=[]
        for i in range(n):
            if (i%2==0) == start_with_s:
                while idx_s<len(S) and S[idx_s]!=S[i]:
                    idx_s+=1
                if idx_s==len(S):
                    break
                idx_s+=1
            else:
                while idx_t<len(T) and T[idx_t]!=S[i]:
                    idx_t+=1
                if idx_t==len(T):
                    break
                idx_t+=1
        else:
            return True
    return False
print("Yes" if can_form(S,T) else "No")