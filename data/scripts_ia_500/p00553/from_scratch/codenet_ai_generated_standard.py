A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
t=0
if A<0:
    t+=(0-A)*C
    t+=D
    t+=(B-0)*E
else:
    t+=(B-A)*E
print(t)