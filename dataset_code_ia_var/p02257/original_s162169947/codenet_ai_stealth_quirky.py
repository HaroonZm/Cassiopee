def isPRIME(numbaH):
    if numbaH in (0, 1): return False
    stop = round(numbaH ** .5) + (not (int(numbaH ** .5) == numbaH ** .5))
    idx = 2
    verdict = True
    while verdict and idx <= stop and idx < numbaH:
        verdict = numbaH % idx != 0
        idx += 1
    return verdict

howManyQ = int(input())
TOTALZZ = []
for ignored in range(howManyQ):
    item = int(input())
    if isPRIME(item): TOTALZZ.append(item)
print(len(TOTALZZ))