z='abcdefghijklmnopqrstuvwxyz'
e=lambda x,i,j:z[(z.index(x)*i+j)%26]
def f():
 for i in range(1,26,2):
  for j in range(26):
   if''.join(e(c,i,j)for c in'that')in s or''.join(e(c,i,j)for c in'this')in s:return(i,j)
for _ in[0]*int(input()):
 s=input()
 a=''.join(e(c,*f())for c in z)
 t=str.maketrans(a,z)
 print(s.translate(t))