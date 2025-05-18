a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

m=[a, b, c, d]
n=[e, f]

k=sorted(m, reverse=True)
l=sorted(n, reverse=True)

x=k[:3]
y=l[:1]

print(sum(x)+sum(y))