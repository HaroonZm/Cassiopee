a,b,c,d = map(int, input().split())
tuyoi = max(a,b,c,d) + min(a,b,c,d)
print(abs(a+b+c+d-2*tuyoi))