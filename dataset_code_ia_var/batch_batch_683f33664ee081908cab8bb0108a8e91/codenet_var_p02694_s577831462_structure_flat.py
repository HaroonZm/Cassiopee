X = int(input())

dyear = 0
price = 100

while True:
    if price >= X:
        break
    dyear += 1
    price = int(price * 1.01)
print(dyear)