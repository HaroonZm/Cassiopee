i=int(input())
s=0
x=i//500
s+=x*1000
i=i%500
x=i//5
s+=x*5
print(s)