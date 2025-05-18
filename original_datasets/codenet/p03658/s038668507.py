N, K = list(map(int, input().split()))
l = list(map(int, input().split()))
l =sorted(l)[::-1]
print(sum(l[:K]))