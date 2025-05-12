a,b = map(int,input().split())
p,q,r= map(int,input().split())
#後に出会う
d = p*b-(b-a)*q
print(d/(q+r)+b)