R1, R2 = [int(i) for i in input().split()]
R3 = 1 / (1 / R1 + 1 / R2)
print("{:.9f}".format(R3))