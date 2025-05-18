dataW = [] 
dataK = []

for i in range (10):
    a = int(input())
    dataW.append(a)
dataW.sort()
pointW = dataW[9]+dataW[8]+dataW[7]
    
for i in range(10):
    a = int(input())
    dataK.append(a)
dataK.sort()
pointK = dataK[9]+dataK[8]+dataK[7]

print(pointW, pointK)