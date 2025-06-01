V = {0:0,1:6000,2:4000,3:3000,4:2000}
indice = 0
while indice < 4:
    entree = input().strip().split()
    t = int(entree[0])
    n = int(entree[1])
    print(n * V[t])
    indice += 1