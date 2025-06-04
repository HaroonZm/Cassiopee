def max_product_steps():
    """
    Lit le nombre de cas de test de l'utilisateur, puis pour chaque cas de test,
    lit une chaîne représentant un nombre, et effectue les opérations suivantes :

    À chaque étape, le nombre courant (sous forme de chaîne) est séparé entre toutes les paires possibles de chiffres,
    le produit des deux parties (gauche et droite) est calculé, et le maximum parmi ces produits est choisi.
    On remplace alors le nombre courant par ce maximum (sous forme de chaîne). 
    Ce processus continue jusqu'à ce qu'il n'y ait plus qu'un seul chiffre dans la chaîne.
    Le programme affiche alors le nombre total d'étapes nécessaires pour ramener le nombre à un seul chiffre.
    """
    # Demande à l'utilisateur combien de cas de test il souhaite traiter.
    for _ in range(input()):
        # Demande à l'utilisateur la chaîne représentant le nombre courant.
        n = raw_input()
        # Initialise le compteur d'étapes.
        c = 0
        # Boucle tant que le nombre courant a plus d'un chiffre.
        while len(n) > 1:
            # Incrémente le compteur d'étapes.
            c += 1
            maxn = 0
            # Parcourt toutes les façons de couper la chaîne en deux parties non vides.
            for i in range(1, len(n)):
                left = int(n[:i])
                right = int(n[i:])
                product = left * right
                # Garde en mémoire le maximum rencontré parmi tous les produits possibles.
                maxn = max(maxn, product)
            # Met à jour la chaîne avec la nouvelle valeur maximale trouvée.
            n = str(maxn)
        # Affiche le nombre d'étapes nécessaires pour ce cas de test.
        print c

# Appelle la fonction principale.
max_product_steps()