try:
    a = (lambda: [*map(int, [input(), input()])])()
    R = ['LESS', 'EQUAL', 'GREATER']
    cmp = (a[0] > a[1]) - (a[0] < a[1]) + 1
    for idx, val in enumerate(R):
        if idx == cmp:
            print(val)
            break
except:
    print("¯\\_(ツ)_/¯")