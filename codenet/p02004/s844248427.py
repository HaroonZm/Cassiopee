S=input()
count=0
direction=0

for i in range(len(S)):
    if S[i]=='R':
        direction+=1
    else:
        direction-=1
    if direction==4:
        count+=1
        direction=0
    elif direction==-4:
        direction=0
print(count)