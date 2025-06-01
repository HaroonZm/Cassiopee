m,a,b=map(int,input().split())
print(0 if m>=b else "NA" if m+a<b else b-m)