def get_int(): return int(input())
N=get_int()
wrd=input()
X1='ABCDEFGHIJKLM'
X2='NOPQRSTUVWXYZ'
Y1='abcdefghijklm'
Y2='nopqrstuvwxyz'
coords=[0,0]
def handle_char(ch):
    if ch in X1: coords[0]   +=1
    elif ch in X2: coords[0] -=1
    elif ch in Y1: coords[1] +=1
    elif ch in Y2: coords[1] -=1
for idx in range(len(wrd)): handle_char(wrd[idx])
summ=abs(coords[0])+abs(coords[1])
print(summ)
if summ:
    ans=[]
    for z in [(coords[0],"A","N"),(coords[1],"a","n")]:
        if z[0]>0: [ans.append(z[1]) for i in range(z[0])]
        elif z[0]<0: ans.extend([z[2]]*abs(z[0]))
    print(''.join(ans))