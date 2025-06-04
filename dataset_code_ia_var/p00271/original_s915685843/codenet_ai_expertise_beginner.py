while True:
    try:
        line = raw_input()
        numbers = line.split()
        a = int(numbers[0])
        b = int(numbers[1])
        print a - b
    except:
        break