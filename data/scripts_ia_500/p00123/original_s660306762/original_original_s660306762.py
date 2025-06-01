"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0123
"""
import sys

def solve(r500, r1000):
    criteria = [(35.50,  71.0, 'AAA'),
                (37.50,  77.0, 'AA'),
                (40.0,   83.0, 'A'),
                (43.0,   89.0, 'B'),
                (50.0,  105.0, 'C'),
                (55.0,  116.0, 'D'),
                (70.0,  148.0, 'E')]
    rank = None
    for c500, c1000, r in criteria:
        if r500 < c500 and r1000 < c1000:
            rank = r
            break
    if rank == None:
        rank = 'NA'
    return rank

def main(args):
    for line in sys.stdin:
        r500, r1000 = [float(x) for x in line.strip().split()]
        result = solve(r500, r1000)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])