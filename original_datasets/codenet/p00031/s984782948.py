while True:
    try:
        n = int(raw_input())
        print ' '.join([str(1<<i) for i in range(10) if ((n >> i) & 1)])
    except EOFError:
        break