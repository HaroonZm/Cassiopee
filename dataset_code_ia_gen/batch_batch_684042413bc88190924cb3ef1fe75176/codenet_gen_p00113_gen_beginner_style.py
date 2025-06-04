while True:
    try:
        line = input()
        if line == '':
            break
        p, q = map(int, line.split())
        remainder = p % q
        decimals = []
        seen = {}
        pos = 0
        repeating_start = -1
        while remainder != 0:
            if remainder in seen:
                repeating_start = seen[remainder]
                break
            seen[remainder] = pos
            remainder *= 10
            decimals.append(str(remainder // q))
            remainder %= q
            pos += 1
        if remainder == 0:
            print(''.join(decimals))
        else:
            non_repeating = decimals[:repeating_start]
            repeating = decimals[repeating_start:]
            print(''.join(decimals))
            # Prepare the second line with spaces and ^ under repeating part
            line2 = ''
            length = len(decimals)
            for i in range(length):
                if i >= repeating_start:
                    line2 += '^'
                else:
                    line2 += ' '
            print(line2)
    except EOFError:
        break