def bSort(data, n):
    count = [0]
    i = [0]
    do = lambda: [
        [False] if (i.__setitem__(0, i[0]+1) or True) and not flag[0] else 
        [True for j in reversed(range(i[0], n-1)) 
         if data[j+1] < data[j] and not (count.__setitem__(0, count[0]+1) or not data.__setitem__(slice(j, j+2), [data[j+1], data[j]])) and flag.__setitem__(0, True)]
        for flag in [[True]] 
        for _ in iter(lambda: flag[0], False)
    ]
    while 1:
        do()
        return count[0]

try:
    from builtins import input
except ImportError:
    input = raw_input

getn = lambda: int(input())
getarr = lambda n: list(map(int, [input() for __ in range(n)]))
while True:
    n = getn()
    if n == 0:
        break
    arr = getarr(n)
    print((lambda a, b: bSort(a, b))(arr, n))