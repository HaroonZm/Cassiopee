while True:
    s = raw_input()
    if s == "#":
        break
    min_value = 10**9
    for start in range(2):
        count = 0
        previous = (int(s[0]) - 1) % 3
        direction = start
        for ch in s[1:]:
            current = (int(ch) - 1) % 3
            if (direction == 0 and previous < current) or (direction == 1 and previous > current):
                count += 1
            else:
                direction = 1 - direction
            previous = current
        if count < min_value:
            min_value = count
    print min_value