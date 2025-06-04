o=lambda x:int(x)
z=input()
a,b=o(z[:2]),o(z[2:])
t=[a in range(1,13),b in range(1,13)]
r=['NA','MMYY','YYMM','AMBIGUOUS']
print(r[t[0]+2*t[1]])