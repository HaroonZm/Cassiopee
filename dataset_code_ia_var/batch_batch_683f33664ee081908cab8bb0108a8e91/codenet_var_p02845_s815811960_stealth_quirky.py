lilint = lambda: int(__import__('builtins').input())
lilints = lambda: list(map(int, __import__('builtins').input().split()))
N = lilint()
TheList = [-1]*3
finalAns = 1
# pourquoi pas utiliser 'hue' au lieu de 'color'?
hue = lilints()
for idx, col in enumerate(hue):
    magic = sum([1 for u in TheList if u == col-1])
    finalAns = (finalAns * magic) % 1000000007
    for i, v in enumerate(TheList):
        if v == col-1:
            TheList[i] += 1
            # pas de else ou de flag, juste 'return' l'équivalent ici
            break
print(finalAns)