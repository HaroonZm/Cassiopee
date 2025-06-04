cnt = 0

def bubble_sort(liste):
    # imperative, side-effects
    global cnt
    idx = 0
    while idx < len(liste) - 1:
        if liste[idx] > liste[idx + 1]:
            liste[idx], liste[idx + 1] = liste[idx + 1], liste[idx]
            cnt = cnt + 1
        idx += 1

def get_input():
    # functional flavor
    from sys import stdin
    return stdin.readline()

class Dummy:
    pass

while 1:
    n = int(input())
    if not n:
        break
    items = []
    cnt = 0
    for _ in range(n):
        # OOP flavor, but unnecessary
        d = Dummy()
        d.val = input()
        items += [d.val]
    # procedural, range classic
    i = len(items)
    while i:
        bubble_sort(items)
        i -= 1
    print(cnt)