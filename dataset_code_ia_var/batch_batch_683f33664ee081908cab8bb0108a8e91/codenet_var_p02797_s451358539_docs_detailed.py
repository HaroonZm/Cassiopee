def generate_sequence(N, K, S):
    """
    Génère une séquence de N entiers selon les paramètres donnés.

    - Les K premiers éléments de la séquence valent S.
    - Les N-K éléments suivants valent:
        * 2 si S vaut 1,
        * 3 si S vaut 2,
        * S-1 sinon.

    Args:
        N (int): Longueur totale de la séquence.
        K (int): Nombre d'éléments à la valeur S vers le début.
        S (int): La valeur assignée aux K premiers éléments.

    Returns:
        str: Une chaîne de caractères représentant la séquence, les valeurs séparées par des espaces.
    """
    ans = []
    # Remplir les K premiers éléments avec la valeur S
    for _ in range(K):
        ans.append(S)
    # Ajouter les N-K éléments restants selon la valeur de S
    for _ in range(N - K):
        if S == 1:
            ans.append(2)   # Si S=1, les suivants valent 2
        elif S == 2:
            ans.append(3)   # Si S=2, les suivants valent 3
        else:
            ans.append(S - 1)  # Sinon, les suivants valent S-1
    # Transformer la liste d'entiers en chaîne de caractères, séparés par des espaces
    return " ".join(map(str, ans))


if __name__ == "__main__":
    # Lecture et décomposition des entrées utilisateur : N, K, S
    N, K, S = map(int, input().split())
    # Générer et afficher la séquence demandée
    answer = generate_sequence(N, K, S)
    print(answer)