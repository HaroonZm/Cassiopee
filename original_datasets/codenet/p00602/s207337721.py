def initSets(N):
    return [ x for x in range(N) ]

def getRoot(arr, n):
    while arr[n] != n:
        arr[n] = arr[arr[n]]
        n = arr[n]
    return n

def union(arr, n, m):
    a = getRoot(arr, n)
    b = getRoot(arr, m)
    if a != b:
        arr[a] = b

def isSameSet(arr, n, m):
    return getRoot(arr, n) == getRoot(arr, m)

def getFibs():
    fibs = []
    a = 1
    b = 1
    while len(fibs) < 1000:
        c = (a + b) % 1001
        a = b
        b = c
        fibs.append(c)
    return fibs
        
if __name__ == '__main__':
    try:
        FIBS = getFibs()
        while True:
            V, d = list(map(int, input().strip().split()))

            fibs = FIBS[:V]
            arr = initSets(V)

            for i in range(V):
                for j in range(i + 1, V):
                    if abs(fibs[i] - fibs[j]) < d:
                        union(arr, i, j)
            
            subsets = {}
            for i in range(V):
                root = getRoot(arr, i)
                if root in subsets:
                    subsets[root].append(fibs[i])
                else:
                    subsets[root] = [fibs[i]]

            print(len(subsets))

    except EOFError:
        pass