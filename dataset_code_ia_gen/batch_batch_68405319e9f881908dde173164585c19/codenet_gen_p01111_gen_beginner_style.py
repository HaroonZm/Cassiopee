while True:
    b = input()
    if b == '0':
        break
    b = int(b)
    max_len = 1
    start_floor = b

    for length in range(2, b+1):
        # Calculate numerator: b - sum of first (length-1) numbers
        numerator = b - (length*(length-1))//2
        if numerator <= 0:
            break
        if numerator % length == 0:
            first = numerator // length
            if first > 0:
                max_len = length
                start_floor = first

    print(start_floor, max_len)