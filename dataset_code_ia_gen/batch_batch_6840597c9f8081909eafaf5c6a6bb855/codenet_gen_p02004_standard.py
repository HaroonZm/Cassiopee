S=input()
dir=0
count=0
passed=[False,False,False,False]
for c in S:
    dir=(dir+ (1 if c=='R' else -1))%4
    if dir==0:
        if all(passed):
            count+=1
        passed=[False,False,False,False]
    else:
        passed[dir]=True
print(count)