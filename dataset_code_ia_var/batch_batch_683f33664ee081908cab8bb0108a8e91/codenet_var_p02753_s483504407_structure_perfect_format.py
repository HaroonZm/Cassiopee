S = input()
L = [0, 0]
for i in range(3):
    if S[i] == "A":
        L[0] += 1
    else:
        L[1] += 1
if max(L) == 3:
    print("No")
else:
    print("Yes")