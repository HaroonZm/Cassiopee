stack = []

while True:
    try:
        x = input()
        if x == '':
            break
        num = int(x)
        if num == 0:
            car = stack.pop()
            print(car)
        else:
            stack.append(num)
    except EOFError:
        break
    except:
        break