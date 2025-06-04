n = int(input())
p = [int(x) for x in input().split()]

def compter(collection, valeur):
    c = 0
    j = 0
    while j < len(collection):
        if collection[j] >= valeur:
            c = c + 1
        j = j + 1
    return c

i = max(p)
while i >= 0:
    t = compter(p, i)
    if t >= i:
        print(i)
        break
    i -= 1