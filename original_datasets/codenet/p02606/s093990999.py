L, R, d = map(int, input().split())
 
if L%d==0:
    print(int(R/d)-int(L/d)+1)
else:
    print(int(R/d)-int(L/d))