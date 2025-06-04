from operator import itemgetter

a = list(map(int, input().split()))
k = int(input())
*rest, m = sorted(a)
print(sum(rest) + (m << k))