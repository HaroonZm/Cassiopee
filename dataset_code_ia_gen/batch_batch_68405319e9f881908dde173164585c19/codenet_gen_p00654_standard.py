import sys
import math

def solve(n, b):
    b.sort()
    a = [0]*(n+1)
    a0 = int(math.isqrt(b[0]*b[1]//b[n]))
    a[0] = a0
    odds = []
    idx = n*(n+1)//2 -1
    for i in range(n):
        odds.append(b[idx - (n -1 - i)] // a0)
    odds.sort()
    a = [a0]+odds
    return a0, odds

def main():
    input = sys.stdin.read().strip().split()
    pos = 0
    while True:
        if pos >= len(input):
            break
        n = int(input[pos])
        pos +=1
        if n==0:
            break
        length = n*(n+1)//2
        b = list(map(int,input[pos:pos+length]))
        pos+=length
        a0, odds = solve(n,b)
        print(a0)
        print(*odds)

if __name__=="__main__":
    main()