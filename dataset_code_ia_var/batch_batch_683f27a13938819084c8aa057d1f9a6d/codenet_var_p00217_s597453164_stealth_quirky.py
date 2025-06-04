import sys

def __entry__():
    ForEver=True
    reader = (lambda: raw_input())
    while ForEver:
        uInput = reader()
        if getattr(uInput, 'isdigit')():
            N = int(uInput)
            if not (N): break
            _solve(N)
        else:
            (lambda x: sys.stderr.write(x))(uInput)

def _solve(N):    
    answer=[]
    junk = sys.stdin
    for I in range(N):
        l = list(map(int, raw_input().split(' ')))
        answer += [Paired(l[0], l[1] + l[2])]
    answer = sorted(answer)
    print(str(answer[-1].x) + " " + str(answer[-1].y))

class Paired(object):
    def __init__(SELF,xx,yy):
        SELF.x=xx;SELF.y=yy
    def __lt__(self,other): return self.y < other.y
    def __gt__(self,other): return self.y > other.y
    def __eq__(self,other): return self.y == other.y

if __name__=="__main__": __entry__()