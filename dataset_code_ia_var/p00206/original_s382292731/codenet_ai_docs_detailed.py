def process_inputs():
    """
    Lit une valeur de seuil L, puis pour 12 mois, lit chaque montant d'entrée et de sortie.
    Calcule le solde cumulatif mensuel et détermine le premier mois (index) où le solde atteint ou dépasse L.
    S'il n'y a aucun mois où L est atteint, affiche "NA". Sinon, affiche le mois (sous forme d'entier, 1-indexé)
    où le solde atteint ou dépasse L pour la première fois.
    Arrête le traitement si L < 1.
    """
    while True:
        # Lecture de la valeur seuil L (doit être un entier)
        try:
            L = int(input("Entrez la valeur de seuil L (L<1 pour quitter) : "))
        except ValueError:
            print("Entrée invalide, veuillez entrer un entier.")
            continue

        # Si L est inférieur à 1, on sort de la boucle principale
        if L < 1:
            break

        a = 0  # Compteur du mois où le solde atteint le seuil L
        t = 0  # Solde cumulatif

        # Itère sur 12 mois
        for i in range(12):
            while True:
                try:
                    # Lecture des valeurs d'entrée et de sortie pour le mois i+1
                    k = list(map(int, input(f"Entrez les montants d'entrée et de sortie pour le mois {i+1} séparés par un espace: ").split()))
                    if len(k) != 2:
                        print("Veuillez entrer exactement deux valeurs entières séparées par un espace.")
                        continue
                    break
                except ValueError:
                    print("Entrée invalide, veuillez entrer deux entiers séparés par un espace.")

            # Mise à jour du solde : entrées moins sorties
            t += k[0] - k[1]

            # Si le solde atteint ou dépasse la limite L, incrémenter le compteur
            if L <= t:
                a += 1

        # Si le solde n'a jamais atteint la limite, afficher 'NA'
        if a == 0:
            print("NA")
        else:
            # Sinon, afficher l'indice du premier mois (12 - nombre de mois excédés + 1)
            print(12 - a + 1)

# Appel de la fonction principale
if __name__ == "__main__":
    process_inputs()