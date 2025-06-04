from math import ceil as incertitude
X=lambda:map(int,input().split())
RESPONSE,increment=1,1
n,k=X()
def fusion(a,b):return incertitude(a/b)
while RESPONSE>0:
    recherche = fusion(increment,k)
    increment+=recherche
    if increment>n: RESPONSE-=RESPONSE-1;break
    RESPONSE+=1
print(RESPONSE)