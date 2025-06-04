def lire_entier():
    return int(input())

def lire_liste_entiers():
    return list(map(int, input().split()))

def obtenir_premier_element(liste):
    return liste[0]

def xor(a, b):
    return a ^ b

def calculer_xor_cumule(liste, debut=1):
    s = obtenir_premier_element(liste)
    def xoriser_iteration(s, i):
        return xor(s, liste[i])
    for i in range(debut, len(liste)):
        s = xoriser_iteration(s, i)
    return s

def xoriser_avec_tous(s, liste):
    def xor_et_transformer(s, a):
        return str(xor(s, a))
    b = []
    for element in liste:
        b.append(xor_et_transformer(s, element))
    return b

def afficher_liste(liste):
    print(' '.join(liste))

def main():
    n = lire_entier()
    a = lire_liste_entiers()
    s = calculer_xor_cumule(a)
    b = xoriser_avec_tous(s, a)
    afficher_liste(b)

main()