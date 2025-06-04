MOD = 10**9 + 7

def max_milk(a: int, b: int, x: int) -> int:
    """
    Calcule le nombre maximal de bouteilles de lait que Kawabayashi peut boire.

    Principe :
    - On commence avec x bouteilles remplies.
    - Chaque fois qu'on échange a bouteilles vides, on obtient b bouteilles remplies.
    - On veut maximiser le total de bouteilles bues.

    Approche :
    1. Initialement, on boit les x bouteilles remplies, donc total = x.
    2. Les bouteilles vides initiales sont aussi x, car on boit tout de suite.
    3. Tant que le nombre de bouteilles vides >= a, on peut échanger :
       - On échange floor(vides / a) fois le lot d'échange.
       - On reçoit (nombre d'échanges) * b bouteilles remplies (qu'on boit immédiatement).
       - On met à jour le total bu, les bouteilles vides deviennent les bouteilles vides restantes + celles qu'on vient de boire.

    4. On répète jusqu'à plus assez de bouteilles vides pour échanger.

    Cette simulation pourrait être chère s'il fallait faire beaucoup d'itérations,
    mais a > b assure que le nombre de bouteilles vides diminue rapidement,
    donc la boucle finira rapidement même pour de grandes valeurs.

    Enfin, on retourne total modulo 10**9+7.

    Paramètres :
    a (int): nombre de bouteilles vides nécessaires pour un échange
    b (int): nombre de bouteilles remplies reçues par échange
    x (int): nombre initial de bouteilles remplies

    Retour :
    int: total maximal de bouteilles bues modulo 10**9+7
    """
    total = x
    bottles_empty = x  # bouteilles vides après avoir bu les initiales
    
    while bottles_empty >= a:
        num_exchanges = bottles_empty // a  # nombre d'échanges possibles
        total += num_exchanges * b           # on boit les nouvelles bouteilles obtenues
        bottles_empty = bottles_empty % a + num_exchanges * b  # mise à jour bouteilles vides
        
    return total % MOD

# Lecture de l'entrée
a, b, x = map(int, input().split())
# Calcul et affichage du résultat
print(max_milk(a, b, x))