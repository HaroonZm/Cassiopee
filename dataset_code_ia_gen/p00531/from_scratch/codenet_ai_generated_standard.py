A=int(input())
B=int(input())
C=int(input())
D=int(input())
P=int(input())
cost_x = A * P
cost_y = B if P <= C else B + D * (P - C)
print(min(cost_x,cost_y))