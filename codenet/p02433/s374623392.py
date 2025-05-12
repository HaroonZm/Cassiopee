from collections import deque
import sys

def main():
    n=int(input())
    sum_d=0
    aa=deque()
    for _ in range(n):
        qq=list(map(int, input().split()))
        if qq[0]==0:
            aa.appendleft(qq[1])
        elif qq[0]==1:
            aa.rotate(-qq[1])
            sum_d+=qq[1]
        else:
            aa.popleft()
    aa.rotate(sum_d)
    for a in aa:
        print(a)

main()