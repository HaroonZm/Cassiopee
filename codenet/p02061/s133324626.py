import math

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

n = int(input())
ma = int(math.sqrt(10**5))
lis = get_sieve_of_eratosthenes(ma)
l_b = [False]*(10**5+1)
for item1 in lis:
    for item2 in lis:
        if item2 < item1:
            continue
        if item1*item2*3 > 10**5:
            break
        i = 0
        while(item1*item2*(3+i) <= 10**5):
            l_b[item1*item2*(3+i)] = True
            i += 1
for item in lis:
    if item**3 < 10**5:
        l_b[item**3] = False
l_count = [0]*(10**5+1)

for i in range(1,10**5+1):
    if l_b[i]:
        l_count[i] = l_count[i-1] + 1
    else:
        l_count[i] = l_count[i-1]

for _ in range(n):
    num = int(input())
    print(l_count[num])