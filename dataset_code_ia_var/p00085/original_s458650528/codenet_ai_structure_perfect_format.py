from copy import copy

while True:
    n, m_ = [int(i) for i in input().split()]
    if n == 0 and m_ == 0:
        break
    m = m_ - 1
    potato = [i + 1 for i in range(n)]
    while True:
        l = len(potato)
        if l == 1:
            print(potato[0])
            break
        pivot = (m + 1) % l
        if pivot != 0:
            potato = copy(potato[pivot:] + potato[:pivot - 1])
        else:
            potato = copy(potato[:-1])