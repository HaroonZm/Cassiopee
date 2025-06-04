N = int(input())
a = []
for i in range(N):
    a.append(int(input())//10)
max_dist = 0
for i in range(N):
    if max_dist >= i:
        max_dist = max(max_dist, i + a[i])
if max_dist >= N-1:
    max_dist = 0
    for i in range(N):
        if max_dist >= i:
            max_dist = max(max_dist, i + a[N-1-i])
    if max_dist >= N-1:
        print("yes")
    else:
        print("no")
else:
    print("no")