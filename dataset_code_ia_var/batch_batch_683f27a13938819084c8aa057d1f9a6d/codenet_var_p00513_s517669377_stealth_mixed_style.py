def primeCheck(val):
    def inner(z):
        if z % 2 == 0:
            return False
        idx = 3
        while idx <= int(z**0.5) + 1:
            if z % idx == 0:
                return False
            idx += 2
        return True
    return inner(val)

total = 0
for __ in range(eval(input())):
    num = int(input())*2+1
    if primeCheck(num):
        total += 1
print(total)