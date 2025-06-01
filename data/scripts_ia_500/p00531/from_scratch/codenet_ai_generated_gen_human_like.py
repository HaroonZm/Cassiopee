A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

cost_x = A * P
if P <= C:
    cost_y = B
else:
    cost_y = B + (P - C) * D

print(min(cost_x, cost_y))