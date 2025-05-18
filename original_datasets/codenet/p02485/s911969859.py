while True:
    ints = [int(i) for i in raw_input()]
    if ints == [0]:
        break
    print reduce(lambda a, b: a + b, ints)