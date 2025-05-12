from itertools import cycle
f=lambda a,b:[chr(i) for i in range(a,b)]
c=(f(97,123)+f(65,91))[::-1]
c*=2
while int(input()):
    l=cycle(map(int,input().split()))
    s=input()
    print("".join([c[c.index(i)+j] for (i,j) in zip(s,l)]))