r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

while True:
    e = input()
    if not e:
        break
    e = e.strip()
    n = []
    for c in e:
        n.append(r[c])
    total = 0
    for i in range(len(n)):
        if i + 1 < len(n) and n[i] < n[i + 1]:
            total -= n[i]
        else:
            total += n[i]
    print(total)