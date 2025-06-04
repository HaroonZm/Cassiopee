def fun():
 n=int(input())
 for _ in range(n):
  S=input()
  M=len(S)
  st=set()
  idx=1
  while idx<M:
   h=S[:idx];t=S[idx:]
   for H in [h,h[::-1]]:
    for T in [t, t[::-1]]:
     for X,Y in [(H,T),(T,H)]:
      st.add(X+Y)
   idx+=1
  print(len(st))
fun()