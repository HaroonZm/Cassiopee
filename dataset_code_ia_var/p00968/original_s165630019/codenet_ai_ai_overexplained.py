import sys  # Importe le module sys de la bibliothèque standard Python pour manipuler les variables d'environnement et les fonctions système
sys.setrecursionlimit(10**6)  # Définit la limite maximale de récursion à 1 million pour éviter les erreurs de dépassement de pile dans certains algorithmes récursifs

def tl(s):
    '''
    Cette fonction convertit une chaîne de caractères s en une liste ref.
    Chaque élément de ref est une liste à deux éléments : 
    - Si le premier élément est True, alors le second élément est un nombre entier (représentant un chiffre/une séquence de chiffres consécutifs dans s)
    - Si le premier élément est False, alors le second élément est un caractère non numérique de s
    '''
    pre = False  # Booléen pour indiquer si le caractère précédent était numérique (True) ou non (False)
    ref = []     # Liste qui stockera la transformation de la chaîne s
    for i in s:  # Itération de chaque caractère i de la chaîne s
        if ord(i) < 58:  # Utilise la fonction ord pour obtenir le code ASCII de i ; ord('0')=48, ord('9')=57, donc <58 garantit qu'il s'agit d'un chiffre
            if pre:  # Si le caractère précédent était aussi un chiffre
                ref[-1] = [True, ref[-1][1]*10 + int(i)]  # Accumule ce chiffre dans le nombre en construction (ex: pour "12", accumule d'abord 1, puis 12)
            else:  # Si le caractère précédent n'était pas un chiffre
                pre = True  # Indique que l'on est maintenant sur un chiffre
                ref += [[True, int(i)]]  # Ajoute une nouvelle entrée contenant [True, valeur de ce chiffre]
        else:  # Si le caractère n'est pas un chiffre
            ref += [[False, i]]  # Ajoute [False, ce caractère] à la liste
            pre = False  # Le caractère précédent n'est plus un chiffre
    return ref  # Retourne la liste transformée

def main():
    '''
    Fonction principale du programme.
    Lit les entrées, transforme les chaînes, compare, puis affiche des résultats selon une logique lexicographique augmentée.
    '''
    n = int(input())  # Lit un entier n depuis l'entrée utilisateur ; représente le nombre de chaînes à comparer
    pibot = tl(input())  # Lit une chaîne et la convertit à l'aide de la fonction tl en format structuré ; représente la chaîne de référence/pivot

    for _ in range(n):  # Répète l'opération suivante n fois (pour chaque chaîne à comparer)
        temp = tl(input())  # Lit une nouvelle chaîne, la convertit en utilisant tl
        ans = "-"  # Initialise la réponse à "-", valeur par défaut en cas d'égalité ou si la chaîne pivot est "plus petite" ou "égale" selon certains cas

        # On va comparer les deux listes (pibot et temp) élément par élément
        for i in range(len(temp)):  # On parcourt chaque élément d'indice i de temp
            if i >= len(pibot):  # Si temp est plus longue que pibot (pibot n'a plus d'élément à comparer à ce niveau)
                ans = "+"  # temp est considérée "plus grande"
                break  # Sort de la boucle, comparaison terminée

            if pibot[i] == temp[i]:  # Si les deux éléments à la même position sont identiques
                if pibot == temp:  # Si l'intégralité des deux listes est identique
                    ans = "+"  # Elles sont considérées égales -> "+"
                    break  # On termine la comparaison
                continue  # Passe au prochain élément (on continue à comparer les suivants)

            if pibot[i][0] and not(temp[i][0]):  # Si pibot[i] est un nombre et temp[i] un caractère
                ans = "+"  # Le nombre est supérieur au caractère
            elif not(pibot[i][0]) and temp[i][0]:  # Si pibot[i] est un caractère et temp[i] est un nombre
                ans = "-"  # Le caractère est inférieur au nombre
            elif pibot[i][0]:  # Si les deux sont des nombres
                if pibot[i][1] < temp[i][1]:  # Compare les valeurs numériques
                    ans = "+"
                else:
                    ans = "-"
            else:  # Si les deux sont des caractères
                if ord(pibot[i][1]) < ord(temp[i][1]):  # Compare les codes ASCII des caractères
                    ans = "+"
                else:
                    ans = "-"
            break  # On ne compare plus, car la différence a été trouvée

        print(ans)  # Affiche la réponse pour cette chaîne comparée
    return  # Termine la fonction principale

main()  # Appelle la fonction principale pour lancer l'exécution du programme