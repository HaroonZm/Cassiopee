h1,h2 = [int(i) for i in input().split()]
k1,k2 = [int(i) for i in input().split()]
a,b,c,d = [int(i) for i in input().split()]

p1 = a*h1 + c*(h1 // 10) + b*h2 + d*(h2 // 20)
p2 = a*k1 + c*(k1 // 10) + b*k2 + d*(k2 // 20)
if p1 > p2:
    print("hiroshi")
elif p1 < p2:
    print("kenjiro")
else:
    print("even")