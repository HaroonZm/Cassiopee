n = int(input())
s = list(map(int, input().split()))
n_ = 0
i = 0
while i < len(s):
    n_ += 1 / s[i]
    i += 1
print(1 / n_)