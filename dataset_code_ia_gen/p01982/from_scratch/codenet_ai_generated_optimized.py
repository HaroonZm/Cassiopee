import sys
input = sys.stdin.readline

def main():
    while True:
        n,l,r = map(int,input().split())
        if n == 0 and l == 0 and r == 0:
            break
        A = [int(input()) for _ in range(n)]
        count = 0
        for x in range(l,r+1):
            idx = -1
            for i,a in enumerate(A):
                if x % a == 0:
                    idx = i+1
                    break
            if idx == -1:
                count += n%2==0
            else:
                count += idx%2==1
        print(count)
main()