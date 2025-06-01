ball = 'A'

try:
    while True:
        line = input()
        if not line:
            break
        x, y = line.strip().split(',')
        if ball == x:
            ball = y
        elif ball == y:
            ball = x
except EOFError:
    pass

print(ball)