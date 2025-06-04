primes = list(map(lambda x: 0 if x < 2 else 1, range(10001)))
i = 2
while i < 100:
    for j in range(i*i, 10001, i):
        primes[j] = 0
    i += 1

def find_pair(n):
    idx = n
    while idx >= 2:
        if primes[idx-2] and primes[idx]:
            print(f"{idx-2} {idx}")
            return
        idx -= 1

getnum = lambda : int(input())
cont = True
while cont:
    val = getnum()
    if not val:
        cont = False
    else:
        find_pair(val)