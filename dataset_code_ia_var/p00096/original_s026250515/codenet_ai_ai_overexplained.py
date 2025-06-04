# Définition d'une fonction nommée N qui prend un argument appelé n
def N(n):
    # L'expression (n+1) calcule la valeur entière immédiatement supérieure à n
    # L'expression (n+2) ajoute 2 à n; elle est utilisée pour générer le terme suivant
    # L'expression (n+3) ajoute 3 à n; elle est utilisée pour générer le terme encore suivant
    # Les trois termes sont multipliés ensemble : (n+1) * (n+2) * (n+3)
    # Le résultat de cette multiplication est ensuite divisé par 6. 
    # En Python 2, l'opérateur '/' permet la division donnant un flottant si nécessaire
    # La fonction retourne donc le résultat de ce calcul complexe
    return (n+1)*(n+2)*(n+3)/6

# Boucle infinie pour permettre la saisie utilisateur multiple tant qu'aucune exception n'est levée
while True:
    try:
        # Lecture de l'entrée utilisateur, raw_input() récupère toute la ligne saisie
        # La fonction int() convertit la chaîne entrée en un entier
        n = int(raw_input())
        
        # Condition : si la variable n dépasse 2000
        if n > 2000:
            # Dans ce cas, n est remplacé par la valeur 4000 moins n
            # Cela "plie" la plage d'entrée autour de 2000 vers 0
            n = 4000 - n
        
        # Si la nouvelle valeur de n est strictement inférieure à 1001
        if n < 1001:
            # On calcule la fonction N pour n et on l'affiche directement
            print N(n)
        else:
            # Sinon, pour n>=1001, une formule différentielle et plus complexe est appliquée
            # N(2*(n-1000)) calcule la fonction N avec 2 fois (n-1000) comme argument
            # (n-1000) calcule le nombre d'écart par rapport à 1000
            # On soustrait (n-1000) puis 1 du résultat de N(2*(n-1000)), puis on divise par 2
            # Cette valeur corrigée est ensuite soustraite au résultat N(n)
            # print sert à afficher le résultat final de ce calcul
            print N(n) - (N(2*(n-1000)) - (n-1000) - 1)/2
    except:
        # Si une exception quelconque se produit (comme une valeur non entière ou EOF),
        # le programme sort immédiatement de la boucle en utilisant break
        break