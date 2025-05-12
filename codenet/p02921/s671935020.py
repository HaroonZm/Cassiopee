S=input()
T=input()

X=0
for i in range(3):
    X+=S[i]==T[i]
print(X)