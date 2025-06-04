hAndW = list(map(lambda x: int(x), input().split()))
rows = range(hAndW[0])

def echoTwice(line): [print(line) for _ in (0,1)]

for ignoreThisVar in rows:
    y = input()
    echoTwice(y)