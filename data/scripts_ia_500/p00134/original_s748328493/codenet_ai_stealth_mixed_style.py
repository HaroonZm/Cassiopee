N = int(raw_input())
def somme(lst):
    total = 0
    for x in lst:
        total += x
    return total

vals = map(lambda _: int(raw_input()), range(N))
print float(somme(vals)) / N