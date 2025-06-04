import sys

def max_recipes(n, m, recipes):
    # On compte pour chaque ingrédient combien de recettes en ont besoin
    ingredient_count = [0]*m
    for r in recipes:
        for i in range(m):
            if r[i] == '1':
                ingredient_count[i] += 1

    # Vérifions les ingrédients qui ne sont dans aucune recette (impossible d'utiliser les ingrédients seuls)
    # Ce cas ne se produit pas car chaque ligne a au moins un 1
    
    # Le nombre d'ingrédients nécessaire pour les recettes choisies est égal à 2 car les ingrédients sont en pack de 2,
    # donc la somme des besoins pour chaque ingrédient dans les recettes choisies doit être paire.
    
    # Chaque recette est une combinaison binaire de longueur m.
    # Le problème consiste à choisir un sous-ensemble de recettes (différentes) tel que pour chaque ingrédient,
    # le nombre total d'utilisations est pair (0 ou 2).
    #
    # Puisque les ingrédients en pack de 2, pour ne pas gâcher un ingrédient, il faut que pour chaque ingrédient,
    # le nombre total d'utilisation soit multiple de 2.
    #
    # Formulé autrement : somme des vecteurs clés des recettes choisies modulo 2 == 0.
    #
    # On veut donc un maximum de recettes dont la somme binaire (xor) est 0.
    #
    # Le problème est donc : trouver la plus grande sous-ensemble de vecteurs binaire dont le xor est 0.
    #
    # On va utiliser une base vectorielle en GF(2) pour trouver la taille maximum du sous-ensemble avec somme nulle.
    # C'est classique : la dimension du sous-espace généré par les vecteurs est la taille de la base.
    #
    # Le nombre maximum d’éléments formant un sous-ensemble à somme nulle est :
    # - Soit n si la somme totale est 0
    # - Sinon, n-1 (on enlève un vecteur qui empêche la somme d’être nulle)
    #
    # Toutefois, ici la condition est plus stricte : chaque ingrédient utilisé doit être utilisé exactement 2 fois,
    # pas un multiple quelconque (4, 6...) car chaque recette l'utilise au plus 1 fois, on ne peut pas répéter une recette.
    #
    # Donc on veut le sous-ensemble T de recettes de taille k tel que :
    # pour chaque ingrédient j, sum_{i in T} b_i,j = 0 mod 2 (pair).
    #
    # Donc, somme XOR = 0.
    #
    # On peut procéder ainsi :
    # - Construire la base vectorielle des recettes en GF(2).
    # - La dimension de la base est d.
    # - Le nombre total de recettes est n.
    # - Si le XOR total des recettes est 0, on peut prendre toutes les recettes (k=n).
    # - Sinon, on peut prendre toutes sauf un (k=n-1).
    #
    # Mais le problème demande le plus grand sous-ensemble dont la XOR est 0, donc c'est exactement la dimension de l'espace -
    # s'il y a un XOR total nul : n; sinon n -1.
   
    # Calculons le XOR total
    total_xor = 0
    for r in recipes:
        val = 0
        for i, c in enumerate(r):
            if c == '1':
                val |= (1 << i)
        total_xor ^= val

    # Construisons la base en GF(2)
    base = []
    for r in recipes:
        val = 0
        for i, c in enumerate(r):
            if c == '1':
                val |= (1 << i)
        # insertion dans la base
        for b in base:
            val = min(val, val ^ b)
        if val > 0:
            base.append(val)
            base.sort(reverse=True)

    d = len(base)

    if total_xor == 0:
        return n
    else:
        return n-1

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        recipes = []
        for _ in range(n):
            s = input().strip()
            recipes.append(s)
        print(max_recipes(n,m,recipes))

if __name__ == "__main__":
    main()