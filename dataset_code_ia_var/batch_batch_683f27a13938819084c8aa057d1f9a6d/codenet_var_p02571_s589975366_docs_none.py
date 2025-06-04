S = input()
T = input()
D = []
for i in range(len(S) - len(T) + 1):
    SS = S[i:i+len(T)]
    dif = 0
    for j in range(len(T)):
        if T[j] != SS[j]:
            dif += 1
    D.append(dif)
print(min(D))