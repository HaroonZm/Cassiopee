h1,h2=map(int,input().split())
k1,k2=map(int,input().split())
a,b,c,d=map(int,input().split())
H=h1*a+h2*b+(h1//10)*c+(h2//20)*d
K=k1*a+k2*b+(k1//10)*c+(k2//20)*d
if H>K:print("hiroshi")
elif H<K:print("kenjiro")
else:print("even")