import bisect

n = int(input())
num = list(map(int, input().split()))

q = int(input())
for _ in range(q):

    k = int(input())
    if k > num[-1]:
        print(n)
        continue
    else:
        print(bisect.bisect_left(num, k))