while 1:
 a,b,c,d=0,0,int(input()),int(input()) if (int(input())!=0) else (break,0)
 l=[]
 for _ in range(c):
  l+=[list(map(int,input().split()))]
 max_p,x=0,0
 for i in l:
  p=1+(b*i[1]/100) if i[2]==1 else (1+i[1]/100)**b
  if p>max_p:max_p,x=p,i[0]
 print(x)