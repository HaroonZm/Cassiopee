import sys  # Importe le module sys qui fournit des fonctions d'accès au système et à l'entrée/sortie standard

# Définit une fonction d'entrée 'input' qui lit une ligne de l'entrée standard,
# supprime les caractères de fin de ligne, et retourne le résultat comme une chaîne de caractères.
input = lambda: sys.stdin.readline().rstrip()

def main():
    # Lit la première entrée (supposée être un entier n), la convertit en entier avec int()
    n = int(input())
    
    # Lit la deuxième ligne d'entrée, la découpe en une liste de chaînes, 
    # puis mappe chaque élément de cette liste à int pour obtenir une liste d'entiers, et enfin cast en 'list'.
    # Cette liste sera stockée dans la variable 'a'.
    a = list(map(int, input().split()))
    
    # Fait de même avec la troisième ligne de l'entrée pour obtenir la liste 'b'.
    b = list(map(int, input().split()))
    
    # Initialise une variable entière 'ans' à 0, qui va accumuler le total désiré.
    ans = 0
    
    # Boucle 'for' qui itère sur les indices de 0 à n-1 (n exclusive).
    # À chaque itération, la variable 'i' prend la valeur de l'index courant.
    for i in range(n):
        # Si l'élément correspondant dans 'b' est supérieur ou égal à celui dans 'a',
        # alors 'b' peut "couvrir" 'a' complètement à cet indice.
        if b[i] >= a[i]:
            # Ajoute la totalité de a[i] à la réponse car tout 'a[i]' est "utilisé".
            ans += a[i]
            # On soustrait de b[i] la quantité utilisée pour correspondre à 'a[i]'.
            b[i] -= a[i]
            # Maintenant, il peut rester du 'b[i]' pour attaquer 'a[i+1]', alors on vérifie cette possibilité.
            # On regarde si le reste de 'b[i]' est supérieur ou égal à 'a[i+1]'.
            if b[i] >= a[i+1]:
                # Dans ce cas, on peut "détruire" tout 'a[i+1]' grâce au reste de 'b[i]'.
                ans += a[i+1]
                # Met à 0, car tout est consommé.
                a[i+1] = 0
            else:
                # Sinon, il ne reste pas assez de 'b[i]' pour tout faire;
                # on ajoute ce qu'il reste de 'b[i]' à la réponse.
                ans += b[i]
                # On soustrait le montant utilisé à 'a[i+1]'.
                a[i+1] -= b[i]
        else:
            # Si 'b[i]' n'est pas assez pour "détruire" tout 'a[i]',
            # alors on ne peut en utiliser que 'b[i]'.
            ans += b[i]
    # Après la boucle, on affiche la valeur finale de 'ans' avec print()
    print(ans)

# On vérifie si ce fichier de code est le programme principal exécuté,
# plutôt qu'importé comme module dans un autre script.
if __name__ == '__main__':
    main()  # Appelle la fonction 'main' pour lancer le processus principal du programme