N = int(input())
X = list(map(int, input().split()))
X_ = sorted(X)
median_max = X_[N // 2]
median_min = X_[(N // 2) - 1]
if median_max == median_min:
    for i in range(N):
        print(median_max)
else:
    for i in X:
        if median_max > i:
            print(median_max)
        else:
            print(median_min)