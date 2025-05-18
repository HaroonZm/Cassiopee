n=1
r=1
while n !=0 and r!=0:
    n,r=input().split()
    n,r=int(n),int(r)

    card= [[int(i) for i in input().split()] for i in range(r)]
    yama= list(range(n,0,-1))
    
    if n ==0 and r==0:
        break

    for i in range(r):
        p=card[i][0]
        c=card[i][1]
        x=yama[:p-1]
        y=yama[p-1:p-1+c]
        z=yama[p-1+c:] 
      
       
        yama=(y+x+z)
        
    print(yama[0])