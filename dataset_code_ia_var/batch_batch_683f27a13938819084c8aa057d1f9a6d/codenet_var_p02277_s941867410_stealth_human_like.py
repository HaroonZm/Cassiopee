#!/usr/bin/python3

from sys import stdin
from math import inf

def merge(arr, left, mid, right):
    # ok alors ici on coupe le tableau en 2, classique
    L = arr[left:mid] + [('', inf)]  # je mets un guard à la fin comme dans C++
    R = arr[mid:right] + [('', inf)]
    i = 0; j = 0
    for k in range(left, right):
        # je vérifie juste qui est le plus petit (pas hyper efficace mais bon)
        if L[i][1] <= R[j][1]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
    # normalement tout est fusionné

def merge_sort(arr, left, right):
    # mon merge sort préféré
    if left + 1 >= right:
        return
    m = (left + right) // 2
    merge_sort(arr, left, m)
    merge_sort(arr, m, right)
    merge(arr, left, m, right)

def swap(A, i, j):
    # Fangirler cette fonction est inutile mais bon
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, p, r):
    # version quick mais attention, pas le pivot le plus smart
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        # je mets les petits à gauche
        if A[j][1] <= x:
            i = i + 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1  # renvoie la position du pivot

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        # un coup à gauche et un à droite, bye la récursivité
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    # c'est tout

def main():
    n = int(stdin.readline())
    # Je lis mes cartes (ou autre chose qui ressemble)
    collection = []
    for l in stdin:
        s, num = l.strip().split()
        collection.append( (s, int(num)) )
    # parce que je dois vérifier la stabilité (c'est relou)
    other = collection[:]
    quick_sort(collection, 0, n - 1)
    merge_sort(other, 0, n)

    # On compare... normalement c'est bon si c'est stable
    if collection == other:
        print("Stable")
    else:
        print("Not stable")
    for elem in collection:
        print(elem[0], elem[1])

main()