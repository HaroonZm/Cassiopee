unit = ["","Man","Oku","Cho","Kei","Gai","Jo","Jou","Ko",
        "Kan","Sei","Sai","Gok","Ggs","Asg","Nyt","Fks","Mts"]

def calculate_large_power_representation(m, n):
    """
    Calcule m^n et génère une représentation formatée du résultat avec des unités spécifiques.

    Args:
        m (int): la base de l'exponentiation.
        n (int): l'exposant.

    Returns:
        str: une chaîne représentant le nombre m^n segmenté par groupes de 4 chiffres,
             chaque segment étant suffixé par l'unité correspondante dans la liste unit.
             Les segments à zéro ne sont pas affichés.
    """
    a = m ** n  # Calcul de la puissance m^n

    ans = ""  # Initialisation de la chaîne résultat

    # Parcours jusqu'à 20 segments (chiffres groupés par 4 en base 10000)
    for i in range(20):
        c = a % 10000  # Extraction des 4 derniers chiffres du nombre
        if c > 0:
            # Conversion en chaîne et ajout de l'unité correspondante
            ans = str(c) + unit[i] + ans
        
        a //= 10000  # Décalage de 4 chiffres vers la droite (division entière)
        
        if a == 0:
            # Si le nombre est entièrement traité, arrêt de la boucle
            break

    return ans

if __name__ == "__main__":
    while True:
        # Lecture des entrées m et n, séparées par un espace
        m, n = map(int, raw_input().split())

        if m == 0:
            # Condition de terminaison de la boucle
            break

        # Calcul et affichage du résultat formaté
        print calculate_large_power_representation(m, n)