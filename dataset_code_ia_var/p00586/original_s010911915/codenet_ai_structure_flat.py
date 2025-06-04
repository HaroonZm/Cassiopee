while True:
    try:
        s = raw_input()
        parts = s.split()
        a = int(parts[0])
        b = int(parts[1])
        print a + b
    except:
        break