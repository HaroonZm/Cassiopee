L=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
S=input()
Z=list()
for i in range(len(S)):
  Z.append(L[(L.index(S[i])-3)%26])
print(''.join(Z))