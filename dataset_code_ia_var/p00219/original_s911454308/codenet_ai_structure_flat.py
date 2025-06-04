while True:
    n = int(input())
    if n == 0:
        break
    data = [0] * 10
    i = 0
    while i < n:
        v = int(input())
        data[v] += 1
        i += 1
    j = 0
    while j < 10:
        if data[j] == 0:
            print('-')
        else:
            print('*' * data[j])
        j += 1