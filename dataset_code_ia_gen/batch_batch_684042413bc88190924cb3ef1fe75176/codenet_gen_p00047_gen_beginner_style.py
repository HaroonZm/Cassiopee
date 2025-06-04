ball = 'A'

while True:
    try:
        line = input()
        if not line:
            break
        x, y = line.split(',')
        if ball == x:
            ball = y
        elif ball == y:
            ball = x
    except EOFError:
        break

print(ball)