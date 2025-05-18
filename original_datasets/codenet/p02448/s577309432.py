# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_5_A&lang=jp
#  Sorting Tuples : python3
#  2018.11.25 yonezawa

import sys
input = sys.stdin.readline

def main():
    l = []
    for i in range(int(input())):
        (a,b,c,d,e) = map(str,input().split())
        l.append((int(a),int(b),c,int(d),e))
    for a,b,c,d,e in sorted(l):
        print (a,b,c,d,e)
if __name__ == '__main__':
    main()