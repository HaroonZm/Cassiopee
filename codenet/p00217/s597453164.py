import sys
def main():
    while True:
        ipt=raw_input()
        if str.isdigit(ipt):
            n=int(ipt)
            if n==0:    break;
            solve(n)
        else:
            sys.stderr.write(ipt)
def solve(n):
    a=[]
    for _ in range(n):
        tmp=map(int,raw_input().split(" "))
        a.append(Pair(tmp[0],tmp[1]+tmp[2]))
    a.sort()
    print a[-1].x, a[-1].y
class Pair:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __cmp__(self,a):
        return self.y-a.y
if __name__=="__main__":    main()