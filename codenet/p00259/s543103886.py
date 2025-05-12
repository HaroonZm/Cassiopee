import re

p = 0
class N(int):
    def __add__(self,n):
        return N((int(self) + int(n)) % p)
    def __sub__(self,n):
        return N((int(self) - int(n)) % p)
    def __mul__(self,n):
        return N((int(self) * int(n)) % p)
    def __floordiv__(self,n):
        if not n:
            raise ZeroDivisionError
        return self*pow(int(n),p-2,p)

while True:
    s = input()
    p,s = s.split(':')
    p = int(p)
    if not p:
        break
    s = s.replace(' ','')
    try:
        n = eval(re.sub(r'(\d+)',r'N(\1)',s).replace('/','//'))
        print('%s = %s (mod %s)'%(s,n,p))
    except ZeroDivisionError:
        print('NG')