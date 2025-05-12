while True:
    n = int(input())
    if n == 0:
        break
    d = {}
    e = []
    for i in range(n):
        tmp = list(map(int, input().split(' ')))
        if tmp[0] in d:
            d[tmp[0]] += tmp[1] * tmp[2]
        else:
            d[tmp[0]] = tmp[1] * tmp[2]
            e.append(tmp[0])
 
    if max(d.values()) < 1000000:
        print('NA')
    else:
        for k in e:
            if d[k] >= 1000000:
                print(k)