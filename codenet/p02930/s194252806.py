n = int(input())
for i in range(n):
  now = []
  I = '0' * (11-len(bin(i))) + bin(i)[2:]
  for j in range(i+1,n):
    J = '0' * (11-len(bin(j))) + bin(j)[2:]
    #print(I,J)
    for k in range(9):
      if I[k] != J[k]:
        now.append(9-k)
        break
  print(' '.join(list(map(str,now))))