n=int(input())
s=input()
x=y=0
for c in s:
    if 'A'<=c<='M': y+=1
    elif 'N'<=c<='Z': y-=1
    elif 'a'<=c<='m': x+=1
    else: x-=1
res=[]
if y>0: res.extend(['A']*y)
elif y<0: res.extend(['N']*(-y))
if x>0: res.extend(['a']*x)
elif x<0: res.extend(['n']*(-x))
print(len(res))
print(''.join(res))