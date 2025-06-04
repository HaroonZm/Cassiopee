import sys
input=sys.stdin.readline

MOD1=10**9+7
MOD2=10**9+9
BASE=131

S=input().strip()
n=len(S)

# Pré-calcul des puissances et hashs prefix
power1=[1]*(n+1)
power2=[1]*(n+1)
h1=[0]*(n+1)
h2=[0]*(n+1)

for i in range(n):
    power1[i+1]=(power1[i]*BASE)%MOD1
    power2[i+1]=(power2[i]*BASE)%MOD2
    h1[i+1]=(h1[i]*BASE + (ord(S[i])-97))%MOD1
    h2[i+1]=(h2[i]*BASE + (ord(S[i])-97))%MOD2

def get_hash(l,r):
    x1=(h1[r] - h1[l-1]*power1[r-l+1])%MOD1
    x2=(h2[r] - h2[l-1]*power2[r-l+1])%MOD2
    return (x1,x2)

Q=int(input())
out=[]

for _ in range(Q):
    l,r,t=map(int,input().split())
    length=r-l+1
    if t==length:
        # Toute chaîne est périodique de longueur égale
        out.append("Yes")
        continue
    # On regarde si on peut modifier au plus un caractère pour que s[l:r] soit périodique de période t
    # On compare segment s[l:l+length-t-1] avec s[l+t:r-1], on compte les différences. Si <=1 alors Yes
    # Pour optimiser on utilise des bisect ou un segment tree serait trop lourd, on fait un binaire sur les différences entre les 2 segments
    # En fait on va itérer sur la substring avec stride t et compter les différences. Mais cela serait O(length/t)
    # Pour speed, on ne peut pas faire grand chose, mais t<=length donc optimal est O(length/t)
    diff=0
    # vérifier les caractères qui devraient être identiques
    for i in range(length - t):
        if S[l-1+i]!=S[l-1+i+t]:
            diff+=1
            if diff>1:
                break
    out.append("Yes" if diff<=1 else "No")

print("\n".join(out))