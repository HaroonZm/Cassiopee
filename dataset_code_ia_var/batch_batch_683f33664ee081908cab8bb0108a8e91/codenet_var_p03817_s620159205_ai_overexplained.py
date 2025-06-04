def main():
    # Demander à l'utilisateur de saisir une valeur, lire la saisie clavier standard (input() renvoie une chaîne de caractères)
    # Convertir la chaîne saisie en valeur entière avec int()
    x = int(input())  # x contiendra le nombre entier saisi par l'utilisateur

    # Calculer combien de fois 11 tient dans x en division entière (//), c'est-à-dire nombre de segments complets de 11 dans x
    # Multiplier ce résultat par 2, car chaque segment de 11 nécessite 2 unités pour la solution désirée
    ans = (x // 11) * 2  # ans représente la réponse partielle basée sur les segments complets de 11

    # Vérifier si le reste de la division de x par 11 est 0 (opérateur % donne le reste) :
    if x % 11 == 0:
        # Si le reste est nul, cela signifie que x est un multiple exact de 11,
        # donc aucune unité supplémentaire n'est nécessaire, on ne fait rien (pass)
        pass
    # Sinon, vérifier si le reste de x divisé par 11 est inférieur ou égal à 6
    elif x % 11 <= 6:
        # Si le reste est entre 1 et 6 inclus, on ajoute 1 unité supplémentaire à ans
        ans += 1  # Ajouter une unité au compteur ans pour couvrir le reste
    else:
        # Si le reste est strictement supérieur à 6 (c'est-à-dire entre 7 et 10), on ajoute 2 unités supplémentaires à ans
        ans += 2  # Ajouter deux unités pour couvrir le reste plus grand

    # Afficher la réponse finale à l'utilisateur en utilisant print()
    # Cela affiche la valeur courante de ans dans la console
    print(ans)

# Ce bloc conditionnel permet de s'assurer que la fonction main() ne sera exécutée
# que si ce fichier Python est exécuté directement (et non importé en tant que module dans un autre fichier)
if __name__ == '__main__':
    main()  # Appel de la fonction main pour démarrer le processus