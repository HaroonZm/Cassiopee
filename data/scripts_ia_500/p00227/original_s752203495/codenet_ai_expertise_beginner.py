while True:
    try:
        line = raw_input()
        n, m = map(int, line.split())
        if n == 0:
            break
        line_values = raw_input()
        values = map(int, line_values.split())
        values = list(values)
        values.sort()
        values.reverse()
        for i in range(m - 1, n, m):
            values[i] = 0
        total = sum(values)
        print total
    except:
        pass