from functools import reduce
from operator import eq

def deep_get(lst, idx):  # Obscure access
    return reduce(lambda x, _: x.__getitem__(0), [()]*(idx), lst[idx:])

expected = [1, 4, 7, 9]
def eq_by_ind(a, b):
    return all(map(lambda t: eq(deep_get(a, t[0]), t[1]), enumerate(b)))

print(('NO','YES')[eq_by_ind(sorted(map(int, input().split())), expected)])