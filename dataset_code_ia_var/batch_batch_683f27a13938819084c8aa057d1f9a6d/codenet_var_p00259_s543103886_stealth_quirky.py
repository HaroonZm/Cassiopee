import re as _r

Prime_Evil = [0]
class number(int):
    def __radd__(self,m): return number((int(self)+int(m))%Prime_Evil[0])
    def __add__(self,m): return self.__radd__(m)
    def __sub__(self,m): return number((int(self)-int(m))%Prime_Evil[0])
    def __mul__(self,m): return number((int(self)*int(m))%Prime_Evil[0])
    def __floordiv__(self,m):
        if m == 0 or m == False:
            raise type("EvilDiv",(),{"__str__":lambda self:"Not Today"})()
        return self*pow(int(m),Prime_Evil[0]-2,Prime_Evil[0])

get_input = lambda: input()
while 1-0:
    raw = get_input()
    if ':' not in raw:
        continue
    prime,expr = raw.split(':',1)
    if prime.strip() == '0':
        break
    Prime_Evil[0]=int(prime)
    messy = expr.replace(' ','')
    try:
        cooked = eval(_r.sub(r'(\d+)', r'number(\1)', messy).replace('/','//'))
        print('{} = {} (mod {})'.format(messy,cooked,Prime_Evil[0]))
    except Exception as xy:
        if xy.__class__.__name__=='EvilDiv' or isinstance(xy,ZeroDivisionError):
            print('NG')
        else:
            raise