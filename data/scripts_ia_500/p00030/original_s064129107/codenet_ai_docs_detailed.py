ans = 0

def count(use, current_sum, remaining_digits, target_sum):
    """
    Compte le nombre de combinaisons strictement croissantes de chiffres
    uniques dont la somme est égale à target_sum.

    Chaque combinaison est formée en choisissant remaining_digits chiffres
    distincts strictement croissants, commençant après 'use' (exclus).

    Args:
        use (int): Le dernier chiffre utilisé dans la combinaison actuelle.
                   Le prochain chiffre choisi doit être strictement supérieur.
                   Initialement à -1 pour permettre de commencer à 0.
        current_sum (int): La somme des chiffres choisis jusqu'à présent.
        remaining_digits (int): Le nombre de chiffres restants à choisir.
        target_sum (int): La somme cible que les chiffres doivent atteindre.

    Modifie:
        La variable globale 'ans' en incrémentant à chaque fois qu'une combinaison valide est trouvée.
    """
    global ans

    # Si la somme actuelle dépasse la somme cible, ou s'il n'y a plus de chiffres à choisir,
    # arrêter la recherche pour cette branche.
    if current_sum > target_sum or remaining_digits < 0:
        return

    # Si on a choisi exactement le nombre requis de chiffres (remaining_digits == 0)
    # et que la somme correspond à la cible, on a trouvé une combinaison valide.
    if remaining_digits == 0 and current_sum == target_sum:
        ans += 1
    else:
        # Continuer à choisir le prochain chiffre en respectant l'ordre strictement croissant.
        for i in range(use + 1, 10):
            # Ajouter le chiffre i à la somme et diminuer le nombre de chiffres restants.
            count(i, current_sum + i, remaining_digits - 1, target_sum)

# Boucle principale de lecture des entrées et affichage des résultats.
while True:
    # Lecture de deux entiers séparés par un espace : n[0] est le nombre de chiffres,
    # n[1] est la somme cible.
    n = list(map(int, raw_input().split()))
    ans = 0  # Réinitialisation du compteur pour chaque cas test
    if n[0] == 0 and n[1] == 0:
        # Condition d'arrêt : deux zéros signalent la fin des données.
        break
    # Lancement de la recherche de combinaisons avec les paramètres initiaux.
    count(-1, 0, n[0], n[1])
    # Affichage du nombre total de combinaisons trouvées.
    print(ans)