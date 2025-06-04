from bisect import bisect_left

def main():
    N=int(input())
    def to_ints(): return list(map(int, input().split()))
    l = to_ints()
    l.sort()
    index = 0
    res = 0
    while index < N-2:
        elem = l[index]
        j = index+1
        while j < N-1:
            second = l[j]
            idx = bisect_left(l, elem+second)
            res=res+(idx-j-1)
            j+=1
        index+=1
    print(res)

main()