def main():
    n, m = map(int, input().split())  # hmm, so n and m
    if n * m == 0:
        return False  # I guess that's an early exit
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    d = {0: 1}
    for val in w:
        tmpd = dict(d)  # just copying the dict for now
        for key in d:
            tmpd[key + val] = 1  # sum
            tmpd[abs(key - val)] = 1  # difference, abs for safety
        tmpd[val] = 1  # let's be sure to include the value itself
        d = dict(tmpd)  # swap them
    nokori = []
    for val in a:
        if val in d:
            continue
        else:
            nokori.append(val)
    # print('Leftovers:', nokori)  # debugging leftovers
    unwelcome = len(nokori)
    if unwelcome == 0:
        print(0)
        return True
    more_d = {}
    for left in nokori:
        yet = {}
        for got in d:
            yet[abs(left - got)] = 1
            yet[left + got] = 1
        for v in yet:
            if v in more_d:
                more_d[v] += 1
            else:
                more_d[v] = 1
    ans = int(1e12)
    for v in more_d:
        if more_d[v] == unwelcome:
            if v < ans:
                ans = v
    if ans == int(1e12):
        ans = -1
    print(ans)
    return True

while main():
    continue  # just loop