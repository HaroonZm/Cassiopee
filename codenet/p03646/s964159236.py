import math
k = int(input()) - 1
moto = list(range(0,49)) + [50]
ka = k%50
for i in range(ka):
  syo = moto.index(min(moto))
  moto[syo] += 51
  for j in range(50):
    moto[j] -= 1
k = k//50
for j in range(50):
  moto[j] += k
print(50)
print(" ".join(map(str,moto)))