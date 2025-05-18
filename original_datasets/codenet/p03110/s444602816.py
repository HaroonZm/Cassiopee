Y = 0
for i in range(int(input())):
    x, u = input().split()
    if u == "JPY":
        Y += int(x)
    if u == "BTC":
        Y += float(x)*380000.0
print(Y)