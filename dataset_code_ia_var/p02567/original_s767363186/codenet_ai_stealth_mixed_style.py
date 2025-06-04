import sys
from typing import List, Callable, TypeVar

input=sys.stdin.readline
T=TypeVar('T')

def _identity(): return lambda x: x

class Segmenter:
    def __init__(self, arr, func, default):
        self.n=len(arr)
        sz=1
        while sz<self.n: sz<<=1
        self.size=sz
        self.buf=[default()for _ in range(2*sz)]
        for i in range(self.n): self.buf[sz+i]=arr[i]
        self.f=func; self.e=default
        for j in range(sz-1,0,-1): self.buf[j]=self.f(self.buf[j<<1], self.buf[(j<<1)|1])
    @classmethod
    def blank(cls, count, func, default): return cls([default for _ in range(count)], func, default)
    def upd(self,pos,val):
        k=pos+self.size; self.buf[k]=val
        while k>1:
            k>>=1
            self.buf[k]=self.f(self.buf[2*k],self.buf[2*k+1])
    def __call__(self,p):
        return self.buf[p+self.size]
    def query(self,lo,hi):
        L,R=self.e(),self.e()
        lo+=self.size; hi+=self.size
        while lo<hi:
            if lo&1: L=self.f(L,self.buf[lo]); lo+=1
            if hi&1: hi-=1; R=self.f(self.buf[hi],R)
            lo>>=1; hi>>=1
        return self.f(L,R)
    def all(self): return self.buf[1]
    def find_right(self,s,f):
        v=self.e()
        idx=s+self.size
        if not f(v): return s
        n=self.n
        while True:
            while idx%2==0: idx>>=1
            if not f(self.f(v,self.buf[idx])):
                while idx<self.size:
                    idx<<=1
                    if f(self.f(v,self.buf[idx])):
                        v=self.f(v,self.buf[idx])
                        idx+=1
                return idx-self.size
            v=self.f(v,self.buf[idx])
            idx+=1
            if (idx&-idx)==idx: break
        return n
    def find_left(self,r,f):
        v=self.e()
        idx=r+self.size
        while True:
            idx-=1
            while idx>1 and idx%2: idx>>=1
            if not f(self.f(self.buf[idx],v)):
                while idx<self.size:
                    idx=(idx<<1)|1
                    if f(self.f(self.buf[idx],v)):
                        v=self.f(self.buf[idx],v)
                        idx-=1
                return idx+1-self.size
            v=self.f(self.buf[idx],v)
            if (idx&-idx)==idx: break
        return 0

def main():
    n,q=[int(s)for s in input().split()]
    arr=[*map(int,input().split())]
    st = Segmenter(arr, max, lambda:-1)
    for _ in range(q):
        v = list(map(int,input().split()))
        if v[0]==1:
            st.upd(v[1]-1,v[2])
        elif v[0]==2:
            print(st.query(v[1]-1,v[2]))
        else:
            print(st.find_right(v[1]-1,lambda x:x<v[2])+1)
main()