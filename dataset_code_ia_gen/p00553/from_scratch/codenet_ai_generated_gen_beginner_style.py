A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

time = 0
temp = A

if temp < 0:
    # chauffer jusqu'à 0
    time += C * (-temp)
    temp = 0
    # dégel à 0
    time += D
    # chauffer jusqu'à B
    time += E * (B - temp)
else:
    # chauffer directement jusqu'à B
    time += E * (B - temp)

print(time)