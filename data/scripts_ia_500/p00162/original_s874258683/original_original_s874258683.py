def two(n):
    if n == 1:
        return True
    elif n%2 != 0:
        return three(n)
    else:
        q = n/2
        return two(q)

def three(n):
    if n == 1:
        return True
    elif n%3 != 0:
        return five(n)
    else:
        q = n/3
        return three(q)

def five(n):
    if n == 1:
        return True
    elif n%5 != 0:
        return False
    else:
        q = n/5
        return two(q)

while True:
    input_line = raw_input()
    if input_line == '0': break
    m, n = map(int, input_line.split())
    c = 0
    for n in range(m, n+1):
        if two(n):
            c += 1
    else:
        print c