import bisect

def main():
    n = int(input())
    li = [int(a) for a in input().split()]
    q = int(input())

    for _ in range(q):
        k = int(input())
        l = bisect.bisect_left(li, k)
        u = bisect.bisect_right(li,k)
        print("{0} {1}".format(l, u))
main()