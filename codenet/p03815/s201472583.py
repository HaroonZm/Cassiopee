a = int(input())
s = (a//11)*2
if 0<a%11<= 6:
    s+=1
elif 7<=a%11 <=10:
    s+=2
print(s)