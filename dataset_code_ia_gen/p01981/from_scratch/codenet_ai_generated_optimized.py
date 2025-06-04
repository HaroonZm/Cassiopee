while True:
    line = input().strip()
    if line == '#':
        break
    g, y, m, d = line.split()
    y, m, d = int(y), int(m), int(d)
    if g == 'HEISEI':
        if y < 31 or (y == 31 and m <= 4 and d <= 30):
            print('HEISEI', y, m, d)
        else:
            if y == 31 and m == 5 and d == 1:
                print('?', 1, 5, 1)
            else:
                diff = (y - 31) * 12 * 31 + (m - 5) * 31 + (d - 1)
                # Calculate new year and date based on diff in days counting approximately, but safer is to process year accurately:
                # But the problem states valid inputs, so we can just do:
                new_y = y - 30
                print('?', new_y, m, d)