def read_and_sum_durations(num_entries: int = 4) -> int:
    """
    Lit un nombre donné de durées (en secondes) à partir de l'entrée standard,
    les convertit en entiers et renvoie leur somme.

    Args:
        num_entries (int): Le nombre de durées à lire (défaut : 4).

    Returns:
        int: La somme totale des durées en secondes.
    """
    # Initialisation de la somme totale à zéro.
    total = 0
    # Lecture de chaque durée individuelle.
    for _ in range(num_entries):
        # Lecture de la durée saisie par l'utilisateur, conversion en entier puis ajout à la somme totale.
        total += int(input())
    # Renvoi de la somme totale des durées saisies.
    return total

def print_duration_in_minutes_and_seconds(total_seconds: int) -> None:
    """
    Convertit un temps total donné en secondes en minutes et secondes,
    puis affiche les résultats.

    Args:
        total_seconds (int): Le temps total à convertir (en secondes).
    """
    # Calcul du nombre entier de minutes.
    minutes = total_seconds // 60
    # Calcul du nombre de secondes restantes.
    seconds = total_seconds % 60
    # Affichage du nombre de minutes.
    print(minutes)
    # Affichage du nombre de secondes restantes.
    print(seconds)

def main():
    """
    Fonction principale :
    1. Lit quatre durées en secondes auprès de l'utilisateur.
    2. Affiche la somme exprimée en minutes et secondes.
    """
    # Lecture et somme des durées saisies par l'utilisateur.
    total = read_and_sum_durations()
    # Affichage de la somme totale en minutes et secondes.
    print_duration_in_minutes_and_seconds(total)

# Exécution de la fonction principale si ce script est exécuté directement.
if __name__ == "__main__":
    main()