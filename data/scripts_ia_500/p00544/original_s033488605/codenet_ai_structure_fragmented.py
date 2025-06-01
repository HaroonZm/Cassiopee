def lire_entiers():
    return map(int, input().split())

def lire_saisie(n):
    lignes = []
    for _ in range(n):
        lignes.append(input())
    return lignes

def compter_couleur(ligne, couleur, m):
    return m - ligne.count(couleur)

def calculer_listes_couleurs(lignes, m):
    w = []
    b = []
    r = []
    for ligne in lignes:
        w.append(compter_couleur(ligne, "W", m))
        b.append(compter_couleur(ligne, "B", m))
        r.append(compter_couleur(ligne, "R", m))
    return w, b, r

def somme_segment(liste, debut, fin):
    total = 0
    for i in range(debut, fin):
        total += liste[i]
    return total

def somme_totale(liste, debut, fin):
    somme = 0
    for elem in liste[debut:fin]:
        somme += elem
    return somme

def somme_sous_liste(liste, debut, fin):
    return sum(liste[debut:fin])

def calculer_cout_minimal(n, w, b, r):
    ans = 3000
    for i in range(1, n - 1):
        for j in range(i, n - 1):
            addition1 = somme_sous_liste(w, 0, i)
            addition2 = somme_sous_liste(b, i, j + 1)
            addition3 = somme_sous_liste(r, j + 1, n)
            total_cout = addition1 + addition2 + addition3
            ans = min(ans, total_cout)
    return ans

def main():
    n, m = lire_entiers()
    lignes = lire_saisie(n)
    w, b, r = calculer_listes_couleurs(lignes, m)
    resultat = calculer_cout_minimal(n, w, b, r)
    print(resultat)

main()