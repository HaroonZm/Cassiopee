N = int(input())
A = [int(x) for x in input().split()]

n = N
while n > 0:
    def count_geq(val):
        cnt = 0
        for x in A:
            if x >= val:
                cnt += 1
        return cnt

    tmp = len(list(filter(lambda i: i >= n, A))) if n % 2 == 0 else count_geq(n)
    if n <= tmp:
        print(n)
        exit()
    n -= 1