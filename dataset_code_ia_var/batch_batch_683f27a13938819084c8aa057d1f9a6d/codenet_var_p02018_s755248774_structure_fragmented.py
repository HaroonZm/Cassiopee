def lire_entier():
    return int(input())

def lire_liste():
    return list(map(int, input().split()))

def est_pair(n):
    return n % 2 == 0

def incrementer(val):
    return val + 1

def traiter_liste(li):
    cnt = creer_compteur()
    for i in li:
        cnt = traiter_element(i, cnt)
    return cnt

def traiter_element(i, cnt):
    if est_pair(i):
        cnt = incrementer(cnt)
    return cnt

def creer_compteur():
    return 0

def afficher(val):
    print(val)

def main():
    n = lire_entier()
    li = lire_liste()
    cnt = traiter_liste(li)
    afficher(cnt)

main()