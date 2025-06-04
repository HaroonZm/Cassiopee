def main():
    """
    Programme principal qui lit les entrées depuis l'utilisateur, puis calcule le nombre minimal
    de transferts nécessaires pour faire passer chaque élément de la liste A à au moins la valeur
    correspondante dans la liste B. Si impossible (somme(A) < somme(B)), affiche -1.

    Entrées :
        - Ligne 1 : entier N, la taille des listes A et B
        - Ligne 2 : liste de N entiers (A)
        - Ligne 3 : liste de N entiers (B)

    Sortie :
        - Un entier correspondant au nombre minimal d'opérations nécessaires,
          ou -1 si la transformation est impossible.
    """
    # Lecture de la taille des listes
    buf = input()
    N = int(buf)  # N éléments dans chaque liste

    # Lecture et conversion de la liste A depuis l'entrée, sous forme d'une chaîne séparée par des espaces
    buf = input()
    buflist = buf.split()
    A = list(map(int, buflist))

    # Lecture et conversion de la liste B depuis l'entrée, sous forme d'une chaîne séparée par des espaces
    buf = input()
    buflist = buf.split()
    B = list(map(int, buflist))

    # Vérifie si la transformation est possible : somme(A) doit être au moins égale à somme(B)
    if sum(A) < sum(B):
        print(-1)  # Transformation impossible si somme insuffisante
        return

    # Calcule la différence entre A[i] et B[i] pour chaque position i
    diff = []
    for i in range(N):
        diff.append(A[i] - B[i])

    # Trie les différences pour séparer facilement surplus et manques
    diff = list(sorted(diff))
    
    # Calcul des besoins en "approvisionnement" (valeurs négatives, manque dans A par rapport à B)
    insufficient_value = 0  # Quantité totale manquante (somme des manques, converties en positif)
    insufficient_count = 0  # Nombre de positions manquantes
    for i in range(N):
        if diff[i] < 0:
            insufficient_value += -diff[i]  # On additionne la valeur manquante
            insufficient_count += 1         # On compte une position à compenser

    deduction_count = 0   # Compte combien de "sources" de surplus on va utiliser pour compenser les manques
    pointer = -1          # Commence par la fin de la différence triée (plus grands surplus)

    # Tant que la somme des surplus n'a pas compensé tous les manques
    while insufficient_value > 0:
        insufficient_value -= diff[pointer]  # Utilise un surplus (diff[pointer] > 0)
        deduction_count += 1
        pointer -= 1

    # Affiche le total minimal d’opérations nécessaires (cas manques + cas surplus utilisés)
    print(insufficient_count + deduction_count)

if __name__ == '__main__':
    main()