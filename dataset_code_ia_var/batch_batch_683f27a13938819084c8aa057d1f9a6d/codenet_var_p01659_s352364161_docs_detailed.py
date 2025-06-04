def main():
    """
    Point d'entrée principal du programme.
    Demande à l'utilisateur une entrée de lignes (non utilisée dans l'algorithme original),
    puis une séquence d'entiers.
    Calcule et affiche le résultat final basé sur l'algorithme décrit ci-dessous.
    """
    input()  # Lecture d'une ligne d'entrée (non utilisée), correspond à la première input()
    ans = 0  # Variable pour compter le nombre d'opérations effectuées
    st = [0]  # Initialise une pile (stack) avec une valeur sentinelle 0

    for a in map(int, raw_input().split()):
        # Tant que la valeur courante 'a' est inférieure au sommet de la pile,
        # dépile les éléments du sommet et incrémente le compteur 'ans'
        while a < st[-1]:
            st.pop()
            ans += 1
        # Si la valeur courante 'a' est supérieure au sommet de la pile,
        # alors empile cette valeur
        if st[-1] < a:
            st.append(a)
    # À la fin, le résultat est la somme du nombre d'opérations effectuées et
    # du nombre d'éléments restants dans la pile (moins la valeur sentinelle)
    print(ans + len(st) - 1)

if __name__ == "__main__":
    main()