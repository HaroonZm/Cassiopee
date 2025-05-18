import re
class c(int):
    global p
    def __add__(self,n):
        return c((int(self)+int(n))%p)
    def __sub__(self,n):
        return c((int(self)-int(n))%p)
    def __mul__(self,n):
        return c((int(self)*int(n))%p)
    def __truediv__(self,n):
        if n==0:raise ZeroDivisionError
        return self*pow(int(n),p-2,p)
  
while 1:
    p,f=input().replace(' ','').split(':')
    p=int(p)
    if p==0:break
    try:print('%s = %s (mod %s)'%(f,eval(re.sub(r'(\d+)',r'c(\1)',f)),p))
    except:print('NG')