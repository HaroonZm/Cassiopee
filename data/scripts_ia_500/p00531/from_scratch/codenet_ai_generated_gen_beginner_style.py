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

if cost_x < cost_y:
    print(cost_x)
else:
    print(cost_y)