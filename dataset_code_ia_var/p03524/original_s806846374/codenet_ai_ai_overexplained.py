def myAnswer(S: str) -> str:
    # Création d'un dictionnaire pour compter le nombre de fois que chaque lettre apparaît dans la chaîne S.
    # Les clés du dictionnaire sont les caractères 'a', 'b' et 'c', et les valeurs initiales sont toutes à 0.
    dic = {'a': 0, 'b': 0, 'c': 0}
    
    # On parcourt chaque caractère 's' dans la chaîne de caractères S, un par un.
    for s in S:
        # On incrémente de 1 la valeur associée à la clé correspondant au caractère 's' dans le dictionnaire.
        # Par exemple, si s == 'a', alors dic['a'] sera augmenté de 1.
        dic[s] += 1
    
    # On récupère les valeurs du dictionnaire (c'est-à-dire le nombre de fois que chaque lettre apparaît),
    # on les trie dans l'ordre décroissant en utilisant la fonction sorted avec reverse=True,
    # et on les stocke dans la liste 'ans'.
    # Par exemple, si dic était {'a': 3, 'b': 1, 'c': 1}, alors ans vaudra [3, 1, 1].
    ans = sorted(dic.values(), reverse=True)
    
    # On calcule la différence entre la valeur maximale et la valeur minimale des comptages.
    # max(ans) donne la plus grande valeur de la liste ans, min(ans) donne la plus petite,
    # donc max(ans) - min(ans) donne l'écart entre le caractère le plus fréquent et le moins fréquent.
    # Si cette différence est supérieure ou égale à 2, on retourne "NO".
    # Sinon, on retourne "YES".
    if (max(ans) - min(ans) >= 2):
        # L'écart est trop grand, donc on retourne la chaîne "NO".
        return "NO"
    else:
        # L'écart est acceptable (0 ou 1), donc on retourne la chaîne "YES".
        return "YES"

def modelAnswer():
    # Cette fonction ne fait rien ; elle exécute simplement l'instruction 'return' pour sortir immédiatement de la fonction.
    return

def main():
    # Demande à l'utilisateur de saisir une chaîne de caractères à l'aide de la fonction input().
    # La valeur saisie par l'utilisateur est stockée dans la variable S.
    S = input()
    
    # Appelle la fonction myAnswer avec l'argument S, puis affiche le résultat avec la fonction print().
    print(myAnswer(S))

# Ce bloc permet de vérifier si ce fichier Python est exécuté comme programme principal (et pas importé comme module).
# Si le fichier est exécuté directement, la fonction main() sera appelée.
if __name__ == '__main__':
    main()