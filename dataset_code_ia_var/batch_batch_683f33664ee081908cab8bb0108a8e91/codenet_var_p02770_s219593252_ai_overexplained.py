import sys  # Importe le module sys pour accéder à des fonctionnalités spécifiques au système, comme sys.stdin

input = sys.stdin.readline  # Redéfinit l'entrée standard pour utiliser sys.stdin.readline qui lit une ligne de l'entrée standard plus efficacement

def main():  # Définit la fonction principale du programme, qui contient la logique principale

    # Lis la première ligne de l'entrée contenant deux entiers séparés par un espace : K et Q
    # map applique la fonction int (transformation en entier) sur chaque élément du résultat de input().split() (sépare la ligne en morceaux sur chaque espace)
    K, Q = map(int, input().split())
    
    # Lis la deuxième ligne, qui contient K entiers séparés par un espace
    # map applique int à chaque élément converti de l'entrée
    # list transforme le résultat de la map en liste
    D = list(map(int, input().split()))
    
    # Boucle pour traiter Q requêtes
    for _ in range(Q):
        # Lis les paramètres d'une requête : n, x, m
        n, x, m = map(int, input().split())
        
        # Calcule le reste modulo m de chaque D[i] et stocke les résultats dans une nouvelle liste md
        md = [D[i] % m for i in range(K)]
        
        smda = 0  # Initialisation d'une variable pour stocker la somme des md[i] pour i dans la première partie de la boucle (voir plus loin)
        mda0 = 0  # Initialise le compteur d'éléments md[i] qui valent zéro dans la même partie
        
        # Boucle sur les éléments md du début jusqu'à l'indice (n-1) % K (exclu)
        for i in range((n - 1) % K):
            # Si md[i] est égal à zéro, incrémente le compteur mda0
            if md[i] == 0:
                mda0 += 1
            # Ajoute md[i] à la somme
            smda += md[i]
        
        # Après la boucle précédente:
        smd = smda    # smd initialise la somme cumulative totale du reste des md sur l'intervalle complet [0, K)
        md0 = mda0    # md0 copie la valeur du nombre d'éléments nuls rencontrés dans la première partie
        
        # Boucle sur les éléments md du précédent index jusqu'à K (pour finir la séquence)
        for i in range((n - 1) % K, K):
            # Si md[i] est nul, incrémente le compteur md0
            if md[i] == 0:
                md0 += 1
            # Ajoute md[i] à la somme totale smd
            smd += md[i]
        
        # Calcule combien de cycles complets de longueur K sont contenus dans les (n-1) premiers éléments
        roop = (n - 1) // K
        
        # Calcule la valeur de res (le résultat final pour la requête)
        # Les différentes parties de la formule:
        # - n - 1 : nombre total d'étapes / éléments à considérer
        # - (x % m) : le reste de x modulo m, utilisé pour le calcul de "débordement"
        # - sum(md) * roop : la somme des valeurs md pour chaque cycle complet multipliée par le nombre de cycles complets
        # - smda : somme des md dans la première section partielle d'éléments
        # - md0 * roop : nombre de zéros dans md sur tous les cycles complets
        # - mda0 : nombre de zéros de la première section partielle
        # La division entière (avec //) fournit combien de fois la somme cumulée dépasse m
        res = n - 1 - (x % m + sum(md) * roop + smda) // m - md0 * roop - mda0
        
        # Affiche le résultat pour cette requête
        print(res)

# Appelle la fonction main pour démarrer le programme lorsque ce fichier est exécuté
main()