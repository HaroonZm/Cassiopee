x=int(input())

y=int(x/11)*2

if x%11>6:
    y+=2
elif x%11>0:
    y+=1

print(y)