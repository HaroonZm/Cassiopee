while True:
    T, P, R = map(int, raw_input().split())
    if T == P == R == 0:
        break
    wrong = [[0 for i in xrange(P)] for j in xrange(T)]
    pen = [[0 for i in xrange(P)] for j in xrange(T)]
    for i in xrange(R):
        t, p, time, mes = raw_input().split()
        t = int(t) - 1
        p = int(p) - 1
        time = int(time)
        if pen[t][p] == 0:
            if mes == 'CORRECT':
                pen[t][p] = wrong[t][p] * 1200 + time
            else:
                wrong[t][p] += 1
    result = []
    for i in xrange(T):
        result.append((p - sum(map(lambda x: x != 0, pen[i])), sum(pen[i]), i + 1))
    result.sort()
    for r in result:
        print r[2], p - r[0], r[1]