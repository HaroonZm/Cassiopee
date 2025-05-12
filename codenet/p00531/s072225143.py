A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X_price = 0
X_price = A * P

Y_price = 0
Y_price += B

if P > C:
    Y_price += (P - C) * D

print(min(Y_price, X_price))