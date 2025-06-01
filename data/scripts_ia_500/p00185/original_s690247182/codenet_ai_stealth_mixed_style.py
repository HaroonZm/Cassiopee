MN = 1000000
mem = [False, False] + [True]*(MN-1)
prime = []

def sieve():
    for i in range(2, MN):
        if mem[i]:
            prime.append(i)
            for j in range(i*2, MN, i):
                mem[j] = False
sieve()

def goldbach_pairs(num):
    count = 0
    for p in prime:
        if p > num // 2:
            break
        if mem[num - p]:
            count += 1
    return count

while True:
    N = input()
    if N == '':
        break
    try:
        N_int = int(N)
    except:
        continue
    print(goldbach_pairs(N_int))