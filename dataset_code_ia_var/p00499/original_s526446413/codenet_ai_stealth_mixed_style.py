import sys
import math

def f(L,a,b,c,d):
 r1=-(-(a)//c)
 r2=math.ceil(b/d)
 return(L-max(r1,r2))

class S:pass

def main(argv):
 L=int(sys.stdin.readline())
 a=int(sys.stdin.readline())
 b=int(sys.stdin.readline())
 c=int(sys.stdin.readline())
 d=int(sys.stdin.readline())
 print(f(L,a,b,c,d))

if __name__=='__main__':
 S.k=main
 S.k(sys.argv[1:])