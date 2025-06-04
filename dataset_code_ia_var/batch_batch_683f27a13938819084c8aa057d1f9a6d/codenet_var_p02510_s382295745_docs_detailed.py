def process_string():
    """
    Lit une chaîne de caractères depuis l'entrée standard, puis un nombre d'opérations à effectuer.
    Pour chaque opération, lit un entier h et effectue une rotation de la chaîne : 
    les h premiers caractères sont déplacés à la fin de la chaîne.
    La fonction s'arrête lorsque la chaîne saisie est le caractère "-".
    Après chaque séquence d'opérations, affiche la chaîne résultante.
    """
    while True:
        # Lit la chaîne de caractères depuis l'entrée utilisateur.
        # Si la chaîne est "-", on stoppe la boucle et donc le traitement.
        n = raw_input()
        if n == "-":
            break

        # Lit le nombre d'opérations à effectuer sur la chaîne.
        m = int(raw_input())

        # Pour chaque opération de rotation :
        for i in range(m):
            # Lit l'entier h pour déterminer la coupure de la chaîne.
            h = int(raw_input())
            # Met à jour n : les h premiers caractères vont à la fin de la chaîne.
            n = n[h:] + n[:h]

        # Affiche la chaîne après toutes les opérations pour cette entrée.
        print(n)

# Appel de la fonction principale si le fichier est exécuté directement.
if __name__ == "__main__":
    process_string()