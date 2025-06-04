def lire_entiers():
    return map(int, input().split())

def lire_nombre():
    return int(input())

def lire_liste(n):
    return [lire_nombre() for _ in range(n)]

def obtenir_k(i):
    return i

def modulo_element(val, k):
    return val % (k+1)

def tester_echange(a, i, k):
    return modulo_element(a[i], k) > modulo_element(a[i+1], k)

def echanger(a, i):
    a[i], a[i+1] = a[i+1], a[i]

def traiter_tour(a, n, k):
    def traiter_un_i(i):
        if tester_echange(a, i, k):
            echanger(a, i)
    for i in range(n-1):
        traiter_un_i(i)

def appliquer_tous_les_tours(a, n, m):
    for k in range(m):
        traiter_tour(a, n, k)

def imprimer_element(x):
    print(x)

def imprimer_liste(a):
    for x in a:
        imprimer_element(x)

def main():
    n, m = lire_entiers()
    a = lire_liste(n)
    appliquer_tous_les_tours(a, n, m)
    imprimer_liste(a)

main()