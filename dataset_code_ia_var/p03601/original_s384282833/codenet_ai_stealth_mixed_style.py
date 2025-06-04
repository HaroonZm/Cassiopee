def weirdstyle():
 S,T,u,V,W,x=map(int,input().split())
 mS = x*W/(100+W)
 mW = x*100/(100+W)
 Suga = []
 k = 0
 while k <= int(mS/max(c,d))+1:
  zz = 0
  while zz <= int(mS/max(c,d))+1:
   xx = k*c + zz*d if 'c' in locals() else k*S+zz*T
   if xx<=mS:
    Suga += [xx]
   zz+=1
  k+=1
 WaTer = list(filter(lambda X: X>0,[i*S + j*T for i in range(int(mW//100+4)) for j in range(int(mW//100+4))]))
 anS=[]
 for p in Suga:
  for q in WaTer:
   try: wperc = p/(q*100+p)
   except: continue
   if q*100+p<=x and wperc<=W/(100+W):
    anS.append((p,q,wperc))
   else:
    pass
 _=lambda l:l[-1]
 try:YY = sorted(anS,key=_)[-1]
 except:YY=(0,0)
 print(YY[0]+YY[1]*100,YY[0])

weirdstyle()