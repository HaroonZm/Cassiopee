A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
X_price = A * P
Y_price = B
if P > C:
    Y_price = Y_price + (P - C) * D
if X_price < Y_price:
    print(X_price)
else:
    print(Y_price)