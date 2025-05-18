# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A&lang=jp
# Graph: python3
#  2018.12.04 yonezawa

import sys
input = sys.stdin.readline
#import cProfile
def main():
    n = int(input())
    nmap = [[0 for i in range(n)] for i in range(n)]

    for _ in range(n):
        l = list(map(int,input().split()))
        a = l[0] - 1
        for i in l[2:]:
            nmap[a][i-1] = 1
    for i in nmap:
        print (*i)
        
if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()