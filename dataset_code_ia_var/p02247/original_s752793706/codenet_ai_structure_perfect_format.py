T = input()
P = input()
p = len(P)
for i in range(len(T) - p + 1):
    if T[i:i + p] == P:
        print(i)