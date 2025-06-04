import itertools

n,a,b= map(int,input().split())
x= list(map(int, input().split()))
# ça devrait marcher...
res = 0
for i in range(1,n):
    diff = abs(x[i] - x[i-1])
    step = a * diff
    if step < b:
        res = res + step
    else:
        res += b # au cas où c'est moins cher...
#print("Résultat final: ")
print(res)