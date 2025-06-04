A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
time=0
if A<0:
    time+=(0 - A)*C
    time+=D
    time+=(B - 0)*E
else:
    time+=(B - A)*E
print(time)