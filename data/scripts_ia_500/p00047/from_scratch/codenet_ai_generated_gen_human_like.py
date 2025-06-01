ball_position = 'A'

try:
    while True:
        line = input()
        if not line:
            break
        cup1, cup2 = line.strip().split(',')
        if ball_position == cup1:
            ball_position = cup2
        elif ball_position == cup2:
            ball_position = cup1
except EOFError:
    pass

print(ball_position)