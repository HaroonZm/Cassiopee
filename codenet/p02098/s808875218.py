a,b=int(input()),int(input())
print((a+b+360*(abs(a-b)>180))/2%360)