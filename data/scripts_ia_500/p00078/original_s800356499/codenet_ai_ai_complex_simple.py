import sys,os,math,functools,itertools,time

class Recurse:
    def __init__(self,fn):
        self.fn=fn
    def __call__(self,*a,**k):
        return self.fn(self,*a,**k)

def pnt(sq,n):
    def pad(x):return ''.join(itertools.islice(itertools.chain(' '*(4)),4-len(x)))+x
    print('\n'.join(''.join(pad(str(x)) for x in row[:n]) for row in sq[:n]))

def cyclic_mod(val,mod):
    return (val+mod)%mod

@Recurse
def build_magic(self,n):
    sq=[[0]*16 for _ in range(16)]
    pos = ((n>>1),(n>>1)+1)
    sq[pos[1]][pos[0]]=1
    def valid(x,y):
        return 0<=x<n and 0<=y<n
    def next_pos(x,y):
        return ((x+1)%n,(y+1)%n)
    def prev_pos(x,y):
        return ((x-1)%n,(y+1)%n)
    i=2
    while i<=n*n:
        x,y=next_pos(*pos)
        while True:
            if not valid(x,y): x,y= x%n,y%n
            if sq[y][x]!=0:
                x,y=prev_pos(x,y)
            if sq[y][x]==0 and valid(x,y):
                break
        sq[y][x]=i
        pos=(x,y)
        i+=1
    return sq

def main():
    if os.environ.get('PYDEV')=="True":
        sys.stdin=open("sample-input.txt")
    for line in itertools.takewhile(lambda x:x!='0', map(str.strip,sys.stdin)):
        n=int(line)
        if n==0:
            break
        sq=build_magic(n)
        pnt(sq,n)

if __name__=="__main__":
    main()