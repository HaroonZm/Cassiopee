T = input()
P = input()
t = len(T)
p = len(P)
for i in range(t - p + 1):
    if T[i:i + p] == P:
        print(i)