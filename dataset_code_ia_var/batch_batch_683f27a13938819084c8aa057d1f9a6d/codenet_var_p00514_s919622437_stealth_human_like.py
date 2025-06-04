# J'utilise math pour les factos mais c'est peut-être overkill... à voir
import math
n, m, r = map(int, input().split())
reste = r - n * m

def combi(x, y):
    if y < 0 or x < y:
        # bon là, c'est pas possible donc 0
        return 0
    # j'espère que factorial ne crash pas pour les grands nombres ?
    return math.factorial(x) // (math.factorial(y) * math.factorial(x - y))

if reste < 0:
    print(0)
else:
    print(combi(reste + n - 1, reste))