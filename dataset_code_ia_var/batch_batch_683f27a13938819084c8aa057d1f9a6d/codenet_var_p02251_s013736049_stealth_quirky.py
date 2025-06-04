S = int(input())
K0IN = (25,10,5,1)
z=0
i=0
while i-len(K0IN):
    t = S//K0IN[i]
    z+=t
    S-=(t*K0IN[i])
    i+=1
print (int(z))