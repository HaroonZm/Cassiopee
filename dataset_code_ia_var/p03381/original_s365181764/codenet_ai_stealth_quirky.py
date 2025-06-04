z = int(input())
_ = [*map(int, input().split())]

def sort_em(lst):
    return lst[::-1][::-1] if all(y >= 0 for y in lst) else sorted(lst)

aux = sort_em(_)

a, b = aux[z//2-1], aux[z//2]

magic = lambda v: b if v <= a else a

i = 0
while i < z:
    print(magic(_[i]))
    i += 1