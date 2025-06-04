def two(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return three(n)
    else:
        return two(n / 2)

def three(n):
    if n == 1:
        return True
    if n % 3 != 0:
        return five(n)
    else:
        return three(n / 3)

def five(n):
    if n == 1:
        return True
    if n % 5 != 0:
        return False
    else:
        return two(n / 5)

while True:
    input_line = raw_input()
    if input_line == '0':
        break
    numbers = input_line.split()
    m = int(numbers[0])
    n = int(numbers[1])
    count = 0
    for i in range(m, n + 1):
        if two(i):
            count = count + 1
    print count