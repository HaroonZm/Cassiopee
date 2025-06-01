def lire_entier():
    return int(input())

def lire_matrice(n):
    matrice = []
    for _ in range(n):
        ligne = lire_liste_entiers()
        matrice.append(ligne)
    return matrice

def lire_liste_entiers():
    return list(map(int, input().split()))

def extraire_colonne(matrice, index):
    colonne = []
    for ligne in matrice:
        colonne.append(ligne[index])
    return colonne

def construire_n(matrice, n_lignes):
    n_list = []
    for i in range(3):
        colonne = extraire_colonne(matrice, i)
        n_list.append(colonne)
    return n_list

def compter_occurrences_valeur_ligne(n_ligne, position_ligne):
    valeur = n_ligne[position_ligne]
    compteur = 0
    for v in n_ligne:
        if v == valeur:
            compteur += 1
    return compteur

def calculer_scores(n, n_lignes):
    scores = [0] * n
    for x in range(3):
        for y in range(n):
            occurences = compter_occurrences_valeur_ligne(n_lignes[x], y)
            if occurences == 1:
                scores[y] += n_lignes[x][y]
    return scores

def afficher_scores(scores):
    for score in scores:
        print(score)

def main():
    N = lire_entier()
    a = lire_matrice(N)
    n_lignes = construire_n(a, N)
    scores = calculer_scores(N, n_lignes)
    afficher_scores(scores)

if __name__ == "__main__":
    main()