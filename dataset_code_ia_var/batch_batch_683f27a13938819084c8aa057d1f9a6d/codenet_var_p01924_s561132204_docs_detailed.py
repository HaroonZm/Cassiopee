def main():
    """
    Point d'entrée principal de la simulation.
    Lit les entrées utilisateur et traite chaque jeu de données jusqu'à ce que T soit 0.
    Pour chaque cas, cela calcule le nombre total de secondes durant lesquelles un point sur la côte
    (situé à distance L du rivage) a été mouillé, en fonction des hauteurs de vagues reçues.
    """
    while True:
        # Lecture des trois entiers : T (nombre d'observations), D (temps de séchage), L (distance du point considéré)
        T, D, L = map(int, input().split())
        
        # Condition d'arrêt : si T vaut 0, on quitte la boucle principale
        if T == 0:
            exit()
        
        # Lecture des T hauteurs de vagues observées à chaque seconde
        XXX = [int(input()) for _ in range(T)]
        
        # Initialisation du compteur de temps pendant lequel le point est mouillé
        total_wet_seconds = 0
        # Temps résiduel pendant lequel le point reste mouillé suite à la dernière vague reçue
        wet_time_remaining = 0
        # Compteur temporaire de la durée consécutive pendant laquelle le point reste mouillé
        consecutive_wet_seconds = 0

        # Parcours des observations de chaque seconde
        for i, wave_height in enumerate(XXX):
            
            # Si le point est encore mouillé d'une vague précédente
            if wet_time_remaining > 0:
                consecutive_wet_seconds += 1
                wet_time_remaining -= 1

            # Si la hauteur de la vague courante atteint ou dépasse la distance L,
            # le point sera mouillé pour les D prochaines secondes
            if wave_height >= L:
                wet_time_remaining = D

            # Si le point vient juste de sécher, on ajoute le cumul au total et on réinitialise le compteur
            if wet_time_remaining == 0:
                total_wet_seconds += consecutive_wet_seconds
                consecutive_wet_seconds = 0
            # Cas particulier : si on est à la dernière observation et que le point est encore mouillé,
            # on ajoute le cumul au total
            elif i == len(XXX) - 1:
                total_wet_seconds += consecutive_wet_seconds

        # Affichage du résultat pour ce jeu de données
        print(total_wet_seconds)


if __name__ == "__main__":
    main()