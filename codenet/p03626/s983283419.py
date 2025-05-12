n = int(input())
sa = input()
sb = input()
p = 1000000007

sal =list(sa)
sal.append("2")
rel =[0]

for i in range(n):
    if rel[-1] ==2:
        rel.append(0)
    elif sal[i] ==sal[i+1]:
        rel.append(2)
    else:
        rel.append(1)

rell =[s for s in rel if s != 0]

if rell[0] ==2:
    res = 6
else:
    res = 3

for j in range(1,len(rell)):
    if rell[j-1] ==2 and rell[j] ==2:
        res = res*3 % p
    elif rell[j-1] ==2 and rell[j] ==1:
        pass
    else:
        res = res*2 % p

print(res)