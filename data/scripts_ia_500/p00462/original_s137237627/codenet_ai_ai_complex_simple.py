import sys, itertools, functools, operator, collections, math
from bisect import bisect_right as br

def main(argv):
    input=sys.stdin.readline
    while 1:
        d=int(input())
        if d==0:break
        n=int(input())
        m=int(input())
        cw_pos=list(itertools.starmap(int,zip(itertools.repeat(input),range(n-1))))
        dests=list(map(int,itertools.starmap(int,zip(itertools.repeat(input),range(m)))))
        cw_pos.extend((0,d))
        cw_pos.sort()
        total_distance=functools.reduce(operator.add,
            map(
                lambda t:
                    0 if t==0 else min(
                        t-cw_pos[br(cw_pos,t)-1],
                        cw_pos[br(cw_pos,t)]-t
                        ),
                dests
            )
        )
        print(total_distance)

if __name__=='__main__':
    main(sys.argv[1:])