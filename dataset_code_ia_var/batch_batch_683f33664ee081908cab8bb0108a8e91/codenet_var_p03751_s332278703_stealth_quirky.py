N=eval(input())
S=[]
for x in '_'*N:S+=[input()]
B=input()
R=[]
def FX(Q,X):
 S=''
 for K in Q:S+=K if K!='?'else X
 return S
F=type('W',(object,),{})()
setattr(F,'A',[B])
setattr(F,'Z',[B])
for t in S:getattr(F,'A').append(FX(t,'a'))
for t in S:getattr(F,'Z').append(FX(t,'z'))
getattr(F,'A').sort()
getattr(F,'Z').sort()
for k in range(N+1):
 if getattr(F,'A')[k]==B:R+=[k+1];break
for k in range(N+1):
 if getattr(F,'Z')[-(k+1)]==B:R+=[N+1-k];break
R.sort()
O=str(R[0])
for q in range(R[1]-R[0]):
 O+=' '+str(R[0]+q+1)
print(O)