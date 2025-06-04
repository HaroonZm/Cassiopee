T=input()
P=input()
for i in range(len(T)-len(P)+1):
    if T[i:i+len(P)]==P:
        print(i)