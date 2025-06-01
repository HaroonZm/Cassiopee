total = 0
while True:
    try:
        line = input()
        number = ''
        for c in line:
            if c.isdigit():
                number += c
            else:
                if number != '':
                    total += int(number)
                    number = ''
        if number != '':
            total += int(number)
    except EOFError:
        break
print(total)