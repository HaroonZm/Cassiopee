import bisect

def main():
    n = int(input())
    A = list(map(int,input().split()))
    q = int(input())
    for _ in range(q):
        b = int(input())
        lb = bisect.bisect_left(A,b)
        ub = bisect.bisect_right(A,b)
        print (lb,ub)

if __name__ == '__main__':
    main()