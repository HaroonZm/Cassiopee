def main():
    """
    Boucle principale du programme qui lit des paires de chaînes de caractères,
    calcule le nombre de "hits" et de "blows" pour chaque paire,
    puis affiche les résultats. La boucle se termine lorsque la première chaîne est "0".
    
    La méthode "hit" compte les positions où les caractères des deux chaînes sont identiques.
    La méthode "blow" compte les caractères présents dans les deux chaînes mais à des positions différentes.
    """
    while True:
        # Lecture de l'entrée utilisateur, deux chaînes séparées par un espace
        r, a = input().split()
        
        # Condition de sortie: si la première chaîne est "0", on termine la boucle
        if r == "0":
            break
        
        # Calcul du nombre de "hit" : caractères identiques à la même position
        hit = 0
        for x, y in zip(r, a):
            if x == y:
                hit += 1
        
        # Calcul du nombre de "blow" :
        # On commence par soustraire les hits, car ils ne comptent pas comme blows
        blow = -hit
        for x in r:
            # Pour chaque caractère dans r, on vérifie s'il existe dans a
            if x in a:
                blow += 1
        
        # Affichage du nombre de hits et blows pour la paire saisie
        print(hit, blow)


if __name__ == "__main__":
    main()