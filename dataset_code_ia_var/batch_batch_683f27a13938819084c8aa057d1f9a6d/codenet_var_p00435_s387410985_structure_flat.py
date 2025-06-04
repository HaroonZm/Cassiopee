L = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
S = input()
Z = []
i = 0
while i < len(S):
    Z.append(L[(L.index(S[i]) - 3) % 26])
    i += 1
print(''.join(Z))