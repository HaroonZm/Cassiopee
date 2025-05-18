K, X = map(int, input().split())
min_x = X - (K-1)
max_x = X + (K-1)
print(" ".join(map(str, list(range(min_x, max_x+1)))))