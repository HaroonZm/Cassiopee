def main():
    """
    Programme principal qui lit des paires de chaînes de caractères,
    compare les caractères à des positions correspondantes
    et compte les correspondances exactes et partielles.
    Le programme s'arrête lorsque la première chaîne est "0".
    
    Le programme fonctionne sur des chaînes de longueur 4.
    Pour chaque paire de chaînes (m, n) :
        - h compte le nombre de caractères identiques à la même position.
        - b compte le nombre de caractères présents dans la seconde chaîne 
          mais à une position différente.
    Les résultats sont affichés sous forme de deux nombres : h et b.
    """
    while True:
        # Lecture de deux chaînes séparées par un espace
        m, n = map(str, raw_input().split())
        
        # Condition d'arrêt lorsque la première chaîne est "0"
        if m == "0":
            break
        
        # Initialisation des compteurs
        h = 0  # nombre de caractères identiques à la même position
        b = 0  # nombre de caractères de m présents ailleurs dans n
        
        # Boucle sur les indices des caractères des chaînes
        for i in range(4):
            if m[i] == n[i]:
                # Caractère identique à la même position
                h += 1
            elif m[i] in n:
                # Caractère présent dans la chaîne n, mais pas à la même position
                b += 1
        
        # Affichage des résultats
        print h, b


# Appel du programme principal
if __name__ == "__main__":
    main()