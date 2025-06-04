def solve(x, n, cnt, hist):
    def to_list(y):
        res = []
        for digit in str(y):
            res += [digit]
        return res
    temp = to_list(x)
    extend_size = n - len(temp)
    idx = 0
    while idx < extend_size:
        temp.append('0')
        idx += 1
    # mélange de style : comprehension puis for classique
    arr = [d for d in temp]
    arr.sort()
    total = 0
    power = 1
    for j in arr:
        total = total + int(j) * power
        power = power * 10
    for k in range(len(arr) - 1, -1, -1):
        total -= int(arr[k]) * (10 ** (len(arr) - 1 - k))
    for pos, val in enumerate(hist):
        if total == val:
            print(pos, total, cnt - pos)
            return None
    hist.append(total)
    # appel recursif en style différent
    return solve(total, n, cnt + 1, hist)

while True:
    s = input().split()
    if s[1] == '0':
        break
    h = [int(s[0])]
    # mélange affectation puis nom des variables variés
    solve(int(s[0]), int(s[1]), 1, h)