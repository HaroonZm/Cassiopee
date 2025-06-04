import sys
import math

def prime_factors(n):
    """
    Retourne la décomposition en facteurs premiers de n sous forme d'un dict {facteur : puissance}
    """
    factors = {}
    # Diviser par 2 tant que possible
    while n % 2 == 0:
        factors[2] = factors.get(2,0) + 1
        n //= 2
    # Essayer les impairs à partir de 3 jusqu'à la racine carrée
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors[f] = factors.get(f,0) + 1
            n //= f
        f += 2
    # Si reste un facteur > 1 c'est un premier
    if n > 1:
        factors[n] = factors.get(n,0) + 1
    return factors

def min_declarations(factors):
    """
    Calcul du nombre minimal de déclarations (minimum)
    => On peut choisir directement un diviseur qui élimine en une fois maximalement d'autres divisors.
    Approche: la déclaration minimale correspond au nombre de facteurs premiers distincts (nombre de p_i)
    car en prenant le produit total des facteurs premiers (sans prendre de puissances plus petites),
    on peut supprimer rapidement toutes les autres possibilités.
    En fait, le minimum est la hauteur minimale d'une chaîne maximale de diviseurs "anti-chaînes".
    
    Or pour ce problème, la démo montre que le minimum est le nombre de facteurs premiers distincts.
    (cf ex pour 18=2*3^2 cela donne 2, pour 99=3^2*11 donne 2, pour un grand nombre premier donne 1)
    
    Pour le minimum: on peut déclarer en premier un nombre premier élevé (ou la multiplication totale),
    puis les autres pour éliminer.
    Comme dans l'exemple donné pour 18: déclarer 9 puis 6 (2 facteurs premiers, correspond bien à 2).
    
    Donc minimum = nombre de facteurs premiers distincts
    """
    return len(factors)

def max_declarations(factors):
    """
    Calcul du nombre maximal de déclarations (maximum)
    => correspond à la longueur maximale d'une chaîne de divisibilité décroissante, en tenant compte de la règle que
    un nombre ne peut être déclaré que s'il n'est divisible par aucun nombre déjà déclaré.
    
    On peut voir que cela correspond à la somme des puissances des facteurs premiers.
    Exemple:
    - 18 = 2^1 * 3^2 => somme des puissances = 3
      Mais l'exemple dit un maximum à 5.
      
    Cependant en lisant attentivement l'exemple:
    - 18 max 5,  
      18 a pour diviseurs : 2,3,6,9,18
      Le maximum est la somme des puissances => 1+2=3 ne marche pas.
      
    La longueur maximale est la somme des puissances multipliée par 1,2,... etc?
    On remarque que :
    L'exemple max pour 18 est 5.
    C'est en fait le nombre total de diviseurs moins 1 :
    Diviseurs de 18 different de 18 : 1,2,3,6,9 donc 5 diviseurs.
    Pas 1, le 1 n'est pas autorisé (car la règle: N以外のNの約数の中から).
    1 est un diviseur de N, mais on ne peut pas le déclarer car c'est pas précisé ? L'exemple omet 1.
    Le 1 est-il déclaré autorisé? On lit "N以外のNの約数" qui signifie tout diviseur de N autre que N
    donc 1 est également possible.
    Mais notons la contrainte "既に宣言したことがある整数の約数になるものは宣言できない"
    - interdir un nombre divisant un nombre déjà déclaré.
    
    Pour le maximum, on peut déclarer les diviseurs dans un ordre compatible avec la contrainte:
    Pas possible de déclarer 3 puis 9 (car 3 divise 9)
    Donc on doit déclarer dans un ordre de divisibilité croissante,
    c'est-à-dire ordre où aucun nombre déclaré plus tard n'est multiple d'un nombre précédent.
    
    Donc le maximum est le nombre total de diviseurs sauf N, 
    mais en respectant la règle qu'on ne peut pas déclarer un nombre qui divise les nombres déjà déclarés.
    En fait, l'ordre inverse: On ne peut pas déclarer d'abord un nombre puis un de ses diviseurs.
    On doit déclarer les diviseurs dans l'ordre strict décroissant, pour maximiser les déclarations.
    
    Exemple 18 :
    Diviseurs (hors 18) : 9,6,3,2,1
    9, 6, 3, 2, 1
    On ne peut déclarer 3 après 9 car 3 divise 9
    Il faut déclarer 9 d'abord, puis 6, 3 impossible, mais 2 possible? 2 ne divise pas 9, ni 6
    Mais 3 divise 6 donc 3 impossible après 6.
    Le maximum trouvé en exemple est 5.
    
    Plus clair: Tous les diviseurs sauf N sont déclarables si on les choisit dans l'ordre inversé de divisibilité.
    
    Calcul : Nombre total de diviseurs = (e1 + 1)*(e2 + 1)*...*(ek + 1)
    On retire 1 (car on ne peut pas déclarer N)
    
    Donc max = nombre total de diviseurs -1
    
    Validé par exemple 18:
    18 = 2^1 * 3^2
    nombre diviseurs = (1+1)*(2+1) = 6
    max = 6 -1 = 5 conforme à l'exemple.
    
    Exemple 99 = 3^2 * 11^1
    total diviseurs = (2+1)*(1+1) = 6
    max = 5 conforme à exemple
    
    Exemple 10000000019 premier => total diviseurs = 2 max=1 ok
    
    Donc max déclaré = total diviseurs - 1
    """
    total_divisors = 1
    for power in factors.values():
        total_divisors *= (power + 1)
    return total_divisors -1

def main():
    # Lecture de l'entrée (N)
    N = int(sys.stdin.readline().strip())
    # Calcul des facteurs premiers
    factors = prime_factors(N)
    # Calcul des résultats minimum et maximum
    mn = min_declarations(factors)
    mx = max_declarations(factors)
    # Affichage des résultats
    print(mn,mx)

if __name__ == "__main__":
    main()