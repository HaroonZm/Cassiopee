while True:
    try:
        line = input()
        if line == "":
            break
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        print(a + b)
    except EOFError:
        break