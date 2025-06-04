from operator import itemgetter

N, L = map(int, input().split())
apples = [L + i for i in range(N)]
excluded = min(apples, key=abs)
print(sum(apples) - excluded)