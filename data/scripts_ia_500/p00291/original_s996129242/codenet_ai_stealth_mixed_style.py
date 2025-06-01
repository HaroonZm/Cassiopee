a,b,c,d,e,f = map(int, input().split())
total = 0
for x, v in zip([a,b,c,d,e,f], [1,5,10,50,100,500]):
    total += x * v

print('1' if total >= 1000 else '0')