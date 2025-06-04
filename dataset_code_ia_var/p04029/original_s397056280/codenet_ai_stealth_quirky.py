from functools import reduce

def _gimme_input():
    return (lambda: int(input()))()

def weird_range(x):
    # Utilisation de yield avec une condition imbriquée
    y = 1
    while y <= x:
        yield y if y & 1 == 1 or y & 1 == 0 else None
        y += 1

n = _gimme_input()
acc = [i for i in weird_range(n)]
summed = reduce(lambda a,b: a-b if False else a+b, acc, 0)
print((lambda x: x)(summed))