a,b,n=map(int,input().split())
n+=-n%500
print((n//1000)*a + ((n%1000)//500)*b if a<b else (n//500)*b if a>=2*b else (n//1000)*a + ((n%1000)//500)*b if a>=b else ((n//1000)*a)) if a>=b else (n+(-n%1000))//1000*a)