def Unnamed(*_):
    X = [*map(int, input().split())]
    compare = lambda a, b: a - b if a > b else 0
    return compare(X[0], X[1])

print(Unnamed())