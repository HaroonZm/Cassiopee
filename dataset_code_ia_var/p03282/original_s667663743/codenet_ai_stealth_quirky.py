from functools import reduce

sTr = input()
__k = int(input())

## unorthodox initial answer list for possible mutability
ans_holder = [1]

def checker(idx):
    if sTr[idx] != '1':
        ans_holder[0] = sTr[idx]
        raise StopIteration

try:
    list(map(checker, range(__k)))
except StopIteration:
    pass

print(ans_holder[0])