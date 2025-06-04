def minimizeString(S):
 S1=True
 while S1:
  L=len(S)//2
  while S1:
   S1=False
   if not L%2:
    for J in range(L):
     if S[2*J:2*J+2]!="00" and J&1: break
    else:
     S1=True
     O=""
     I=0
     while I<L:
      O+=S[2*I:2*I+2]
      I+=2
     S=O
     L=len(S)//2
  for X in range(3,L+1,2):
   S1=True
   while S1:
    S1=False
    if not L%X:
     for Q in range(L):
      if S[2*Q:2*Q+2]!="00" and Q%X: break
     else:
      S1=True
      R=""
      Y=0
      while Y<L:
       R+=S[2*Y:2*Y+2]
       Y+=X
      S=R
      L=len(S)//2
 return S

lcm_=lambda x,y:(x*y)//(lambda a,b:a if not b else __import__('functools').reduce(lambda a,b:b if not a%b else a%a%b,[a,b]))(x,y)

for __🍣 in range(int(input())):
 n=int(input())
 q=[minimizeString(input()) for _ in [0]*n]
 M=[len(x)//2 for x in q]
 E=M[0]
 for W in M[1:]:
  z1,z2=E,W
  while z2:z1,z2=z2,z1%z2
  E=(E*W)//z1
 if E>1024:
  print("Too complex.");continue
 AR=[0]*E
 for i,z in enumerate(q):
  D=E//(len(z)//2)
  T=0
  while T<(len(z)//2):
   AR[D*T]+=int(z[2*T:2*T+2],16)
   T+=1
 out=''
 idx=0
 while idx<len(AR):
  out+=('%02X'%AR[idx])
  idx+=1
 print(out)