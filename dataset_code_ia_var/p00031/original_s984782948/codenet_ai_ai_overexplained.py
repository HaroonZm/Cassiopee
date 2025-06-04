# Commence une boucle infinie, ce qui signifie que le code à l'intérieur de cette boucle sera exécuté à répétition
while True:
    try:
        # Essaie d'exécuter les instructions suivantes, et gère les exceptions éventuelles
        
        # Demande une entrée à l'utilisateur sous forme de chaîne de caractères à l'aide de raw_input()
        # raw_input() est utilisé en Python 2 pour obtenir une saisie clavier en tant que chaîne (string)
        s = raw_input()
        
        # La variable s contient donc la valeur saisie (string)
        # Utilise la fonction int() pour convertir cette chaîne de caractères en entier (int)
        n = int(s)
        
        # Va créer une liste contenant certains éléments selon une condition
        # Utilise une compréhension de liste pour générer cette liste
        
        # range(10) génère une séquence de nombres entiers de 0 à 9 inclus
        # Pour chaque i de 0 à 9 :
        # (n >> i) effectue un décalage à droite (right bit shift) de i positions sur le nombre n
        # Cela déplace les bits de n vers la droite de i positions, ce qui place le bit d'indice i en position 0
        # Ensuite, & 1 effectue un ET binaire (bitwise AND) avec 1, ce qui donne 1 si le bit de poids faible (bit 0) était 1, sinon 0
        # Donc, ((n >> i) & 1) teste si le i-ème bit de n est activé (égal à 1)
        
        # Si le i-ème bit de n est à 1 :
        #     - 1 << i (c'est-à-dire 1 décalé à gauche de i bits) est égal à 2 puissance i
        #     - str(1 << i) convertit ce nombre en chaîne de caractères
        # Donc, crée une liste des puissances de 2 pour lesquelles le bit correspondant de n est à 1
        
        lst = [str(1 << i) for i in range(10) if ((n >> i) & 1)]
        
        # ' '.join(lst) assemble tous les éléments de la liste lst en une seule chaîne de caractères,
        # séparés par un espace (' ')
        # Affiche ensuite le résultat à l'écran avec print (Python 2)
        print ' '.join(lst)
    
    # Capture l'exception EOFError, qui se produit lorsque l'entrée se termine (exemple: Ctrl-D sur Unix)
    except EOFError:
        # Quitte la boucle while et donc le programme
        break