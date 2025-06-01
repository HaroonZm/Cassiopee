h1,h2 = map(int,input().split())
k1,k2 = map(int,input().split())
a,b,c,d = map(int,input().split())
H = a*h1 + b*h2 + c*(h1//10) + d*(h2//20)
K = a*k1 + b*k2 + c*(k1//10) + d*(k2//20)
if H > K:
    print('hiroshi')
elif H < K:
    print('kenjiro')
else:
    print('even')