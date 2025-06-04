now = 'A'
while True:
    try:
        s = input()
        a_b = s.split(',')
        a = a_b[0]
        b = a_b[1]
        if now == a:
            now = b
        elif now == b:
            now = a
    except:
        break
print(now)