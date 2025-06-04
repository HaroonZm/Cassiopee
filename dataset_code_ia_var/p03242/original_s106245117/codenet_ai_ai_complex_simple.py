import bisect,collections,copy,heapq,itertools,math,string
import sys
S = lambda: sys.stdin.readline().rstrip()
M = lambda: map(int,sys.stdin.readline().rstrip().split())
I = lambda: int(sys.stdin.readline().rstrip())
LI = lambda: list(map(int,sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())
N = S()
trans = str.maketrans('19','91')
print(''.join(map(lambda t: ''.join(itertools.compress('91', [t=='1',t!='1'])), N)))