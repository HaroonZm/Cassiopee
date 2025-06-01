while True:
    try:
        n = int(raw_input())
        result = []
        for i in range(10):
            if (n >> i) & 1:
                result.append(str(1 << i))
        print ' '.join(result)
    except EOFError:
        break