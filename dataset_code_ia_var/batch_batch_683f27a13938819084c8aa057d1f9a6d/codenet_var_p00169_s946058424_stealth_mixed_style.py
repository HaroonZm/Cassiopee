import collections

def calcPoints(cards):
    c = collections.defaultdict(int)
    for n in cards:
        c[n] += 1
    total = sum([j * c[j] for j in range(2,10)])
    temp = 0
    i = 10
    while i < 14:
        temp = temp + 10 * c[i]
        i += 1
    total = total + temp
    ace = c[1]
    j = 0
    possible = False
    while j <= ace:
        s = j + (ace-j)*11 + total
        if s <= 21:
            total += j + (ace-j)*11
            possible = True
            break
        j += 1
    if not possible:
        total += ace
    if total > 21: return 0
    return total

cont = 1
while cont:
    s = input()
    if s=='0': cont=0; continue
    arr=[int(x) for x in s.split()]
    res = calcPoints(arr)
    print(res)