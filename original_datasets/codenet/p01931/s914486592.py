N = int(input())
S = input()

kizetu = False
cnt = 0

for s in S:
    
    if s == "x":
        kizetu += 1
    else:
        kizetu = 0
        
    if kizetu == 2:
        print(cnt)
        break
    
    cnt += 1
else:
    print(len(S))