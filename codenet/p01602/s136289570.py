a=0
for _ in range(int(input())):
    b,c=input().split()
    a+=int(c) if b=='(' else -int(c)
    if a<0:break
print('NO' if a else 'YES')