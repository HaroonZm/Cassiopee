def bubble_sort(n, key=0):
    c = 0
    r = [x if isinstance(x, list) else [x] for x in n[:]]
    l = len(r) - 1
    for i in range(0, l):
        for j in range(l, i, -1):
            if r[j][key] < r[j-1][key]:
                r[j], r[j-1] = r[j-1], r[j]
                c += 1
    r = [x[0] if len(x) == 1 else x for x in r]
    return {'list': r, 'count': c}

def selection_sort(n, key=0):
    c = 0
    r = [x if isinstance(x, list) else [x] for x in n[:]]
    l = len(r)
    for i in range(0, l):
        mini = i
        for j in range(i, l):
            if (r[j][key] < r[mini][key]):
                mini = j
        if mini != i:
            r[i], r[mini] = r[mini], r[i]
            c += 1
    r = [x[0] if len(x) == 1 else x for x in r]
    return {'list': r, 'count': c}

def card_format(cards):
    return ' '.join([x[0] + str(x[1]) for x in cards])

if __name__ == '__main__':
    n = int(input())
    c = list(map(list, input().split(' ')))
    c = [[x[0], int(x[1])] for x in c]
    bsc = card_format(bubble_sort(c, 1)['list'])
    ssc = card_format(selection_sort(c, 1)['list'])
    print(bsc)
    print('Stable')
    print(ssc)
    print('Stable' if bsc == ssc else 'Not stable')