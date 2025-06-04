balls = [1,0,0]
while True:
    try:
        line = input()
        parts = line.split(',')
        a = parts[0]
        b = parts[1]
        i1 = ord(a) - ord("A")
        i2 = ord(b) - ord("A")
        temp = balls[i1]
        balls[i1] = balls[i2]
        balls[i2] = temp
    except:
        break
i = 0
while i < 3:
    if balls[i]:
        print(chr(i + ord("A")))
    i += 1