def rotate_string(C: str, rotations: list) -> str:
    """
    Effectue une série de rotations sur la chaîne de caractères donnée.

    Args:
        C (str): La chaîne de caractères initiale à faire tourner.
        rotations (list): Liste des entiers représentant chaque rotation
                          (nombre de caractères à couper du début et à mettre en fin).

    Returns:
        str: La chaîne de caractères modifiée après toutes les rotations.
    """
    # Pour chaque valeur de rotation donnée, on applique la rotation sur la chaîne
    for H in rotations:
        # Effectue la rotation en prenant une sous-chaîne de C à partir de l'indice H
        # puis en ajoutant le début de la chaîne (jusqu'à l'indice H) à la fin.
        C = C[H:] + C[:H]
    return C

def main():
    """
    Exécute une boucle interactive qui effectue des rotations de chaînes
    selon les instructions de l'utilisateur jusqu'à ce que '-' soit entré.

    L'utilisateur entre une chaîne, puis un nombre d'opérations à effectuer.
    Pour chaque opération, il entre un nombre d'indices pour la rotation.
    Le résultat de la chaîne après toutes les rotations est affiché.
    """
    while True:
        # Lecture de la chaîne de caractères initiale depuis l'utilisateur
        C = input()
        # Si l'utilisateur entre '-', arrêt de la boucle principale
        if C == "-":
            break
        # Lecture du nombre d'opérations à effectuer
        N = int(input())
        # Liste pour stocker les valeurs de rotation pour cette chaîne
        rotations = []
        for i in range(N):
            # Lecture de la valeur de rotation pour chaque opération
            H = int(input())
            rotations.append(H)
        # Application des rotations à la chaîne
        result = rotate_string(C, rotations)
        # Affichage du résultat final
        print(result)

# Appel du point d'entrée principal lorsque le script est exécuté
if __name__ == "__main__":
    main()