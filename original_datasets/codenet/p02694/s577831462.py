X = int(input())

dyear = 0
price = 100

while price < X:
    dyear += 1
    price = int(price * 1.01)
print(dyear)