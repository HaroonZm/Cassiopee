import collections

N = input()
M = [input()for i in range(int(N))]
X = collections.Counter(M)
max(X.items(), key=lambda x:x[1])[0]
i = max(X.values())
Y = [k for k, v in X.items() if v == i]
b = len(Y)
Z = sorted(Y,key =str.lower)
for i, v in enumerate(Z):
    if i > b:
        break
    else:
        print(Z[i])