import bisect

def main():
    n = int(input())
    li = [int(a) for a in input().split()]
    q = int(input())

    for _ in range(q):
        k = int(input())
        i = bisect.bisect_left(li, k)
        print(i)
        
main()