n = input()
Taro,Hanako = 0,0
for i in range(n):
    t,h = raw_input().split() 
    if t > h :
       Taro += 3
    elif t < h :
        Hanako += 3
    else : 
        Taro += 1
        Hanako += 1
print Taro,Hanako