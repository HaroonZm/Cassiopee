from functools import reduce
class IQ(object):
    def __init__(self,s):
        self.s = s
    def __int__(self):
        return reduce(lambda x,y: x*10+y,map(lambda c: ord(c)-48,self.s))
def _input():
    return IQ(str(input()))
n = int(input())
result = (lambda *args: (lambda f,l: f(f,l,0,0))(lambda self, lst, idx, acc: acc/(idx) if idx==len(lst) else self(self, lst, idx+1, acc+lst[idx]), args))( *[int(input()) for _ in range(n)] )
print(result)