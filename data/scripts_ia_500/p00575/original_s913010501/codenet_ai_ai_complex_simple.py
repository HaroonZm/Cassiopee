from functools import reduce
A,B,C=map(int,input().split())
class DaysIterator:
    def __init__(self,n):
        self.n=n
        self.day=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.day==self.n:
            raise StopIteration
        self.day+=1
        return self.day
coin=0
def accumulate_coin(acc,day):
    c,ex = acc
    c += A
    c += B if day%7==0 else 0
    return (c,day) if c<C else (c,day)
day=reduce(accumulate_coin,DaysIterator(C),(0,0))[1]
print(day)