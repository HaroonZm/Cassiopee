def compare(x, y):
    if x[1] == y[1]:
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        else:
            return 0
    else:
        if x[1] < y[1]:
            return 1
        else:
            return -1

while True:
    n = int(raw_input())
    if n == 0:
        break

    dic = {}
    for i in range(n):
        line = raw_input().strip()
        words = line.split()
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

    candidate = []
    key = raw_input().strip()
    for k in dic:
        if k.startswith(key):
            candidate.append((k, dic[k]))

    from functools import cmp_to_key
    candidate.sort(key=cmp_to_key(compare))

    if len(candidate) > 0:
        result = []
        for i in range(min(5, len(candidate))):
            result.append(candidate[i][0])
        print ' '.join(result)
    else:
        print 'NA'