def p(r):print(r)
z=lambda x:int(x)
L=input().split();[v,w,u]=L[::-2]+[L[1]]
if w=='+':p(z(v)+z(u))
elif w=='-':p(z(v)-z(u))