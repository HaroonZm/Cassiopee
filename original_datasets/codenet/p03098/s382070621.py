N,K=map(int,input().split());p=[int(i)-1 for i in input().split()];q=[int(i)-1 for i in input().split()];T=lambda s,t:[s[t[i]] for i in range(N)];m=[[0 for i in [0]*N] for i in [0]*6];m[0]=p;m[1]=q
def I(s):
 r=[0]*N
 for i in range(N):r[s[i]]=i
 return r
for i in range(4):m[i+2]=T(m[i+1],I(m[i]))
E=lambda s,k:(E(T(s,s),k//2) if k!=0 else list(range(N)))if k%2==0 else T(E(T(s,s),k//2),s);t=E(T(T(T(q,I(p)),I(q)),p),~-K//6);print(" ".join([str(i+1) for i in T(T(t,m[~-K%6]),I(t))]))