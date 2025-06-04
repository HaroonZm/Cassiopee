S = input()
T = input()

X = 0
i = 0
while i < 3:
    if S[i] == T[i]:
        X = X + 1
    i = i + 1
print(X)