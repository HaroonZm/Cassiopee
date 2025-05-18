import itertools

while 1:
    n = int(input())
    k = int(input())
    if n == k == 0:
        break
    a = []
    for i in range(n):
        a.append(input())
    
    b = []
    p = list(itertools.permutations(a, k))
    for i in p:
        b.append(''.join(i))
    c = list(set(b))
    print(len(c))