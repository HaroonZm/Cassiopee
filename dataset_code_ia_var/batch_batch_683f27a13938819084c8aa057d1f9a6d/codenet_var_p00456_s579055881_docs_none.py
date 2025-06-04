W = []
K = []
for i in range(10):
    W.append(int(input()))
for i in range(10):
    K.append(int(input()))
W.sort(reverse=True)
K.sort(reverse=True)
point_W = sum(W[:3])
point_K = sum(K[:3])
print(point_W, point_K)