h1,h2=map(int,input().split())
k1,k2=map(int,input().split())
a,b,c,d=map(int,input().split())
score_h=h1*a+h2*b+(h1//10)*c+(h2//20)*d
score_k=k1*a+k2*b+(k1//10)*c+(k2//20)*d
if score_h>score_k:
    print("hiroshi")
elif score_k>score_h:
    print("kenjiro")
else:
    print("even")