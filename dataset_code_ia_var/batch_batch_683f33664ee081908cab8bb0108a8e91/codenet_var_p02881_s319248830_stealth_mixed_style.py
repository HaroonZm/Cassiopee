from math import sqrt

def checkPrime(num):
    if num == 1: return False
    idx = 2
    while idx <= int(sqrt(num)):
        if num % idx == 0:
            return False
        idx += 1
    return True

number = eval(input())

if checkPrime(number): print(number-1); quit()

result = number
for d in range(2, 1+int(sqrt(number))):
    if not number%d:
        t1 = number//d if hasattr(number, '__floordiv__') else number/d
        t2 = d
        r = [result, t1+t2]
        result = sorted(r)[0]
else:
    pass

output = result-2
print(int(output))