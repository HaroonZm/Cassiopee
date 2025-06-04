#!/usr/bin/env python3

# Importation du module 'array', qui fournit un type de séquence efficace pour stocker des données numériques.
import array

# Importation du module 'bisect', qui fournit des fonctions pour manipuler et rechercher dans des listes triées.
import bisect

# Définition d'une constante qui représente la valeur maximale jusqu'où on veut générer les nombres premiers.
MAX_PRIME = 1299709  # Ceci est le plus grand nombre premier en dessous de 1 300 000.

# Définition de la fonction du crible d'Ératosthène pour générer tous les nombres premiers inférieurs à 'end'.
def sieve_of_eratosthenes(end, typecode="L"):
    # Vérification préalable que la borne supérieure 'end' est strictement supérieure à 1.
    assert end > 1

    # Création d'un tableau de booléens pour indiquer si chaque nombre est premier ou non.
    # Le tableau a la taille 'end' et chaque élément est initialisé à True (supposé premier).
    is_prime = array.array("B", (True for i in range(end)))
    
    # On sait que 0 et 1 ne sont pas des nombres premiers, donc on les marque comme faux.
    is_prime[0] = False
    is_prime[1] = False

    # Création d'un tableau destiné à contenir tous les nombres premiers trouvés.
    # On utilise le type numérique long (typecode 'L') par défaut, mais cela peut être changé.
    primes = array.array(typecode)

    # Boucle principale du crible, démarre à 2 car 0 et 1 ne sont pas premiers.
    for i in range(2, end):
        # Si le nombre courant 'i' est toujours marqué comme premier :
        if is_prime[i]:
            # On ajoute 'i' à la liste des nombres premiers.
            primes.append(i)
            # On marque comme non premiers tous les multiples de 'i', en partant de 2*i.
            for j in range(2 * i, end, i):
                is_prime[j] = False
    # On retourne la liste (tableau) de nombres premiers générés.
    return primes

# Définition de la fonction principale du programme.
def main():
    # Génère tous les nombres premiers jusqu'à MAX_PRIME inclus (on ajoute 1 car la fin du range est exclue).
    primes = sieve_of_eratosthenes(MAX_PRIME + 1)

    # Fonction interne pour déterminer la taille de l'intervalle de nombres premiers qui contient 'n'.
    def length_of_gap_containing(n):
        # Recherche l'indice d'insertion de 'n' dans la liste triée 'primes'.
        # 'bisect_left' retourne l'indice du premier élément >= n.
        index = bisect.bisect_left(primes, n)
        # On récupère le prochain nombre premier qui est >= n.
        next_prime = primes[index]
        # Si 'n' est exactement égal à ce nombre premier, alors il n'y a pas d'intervalle (le nombre est premier).
        if next_prime == n:
            return 0
        else:
            # Sinon, on récupère le nombre premier précédent dans la liste à l'indice juste avant.
            prev_prime = primes[index - 1]
            # Renvoie la différence entre les deux nombres premiers encadrant 'n', c'est-à-dire la taille de l'intervalle.
            return next_prime - prev_prime

    # Boucle infinie pour traiter plusieurs entrées utilisateur.
    while True:
        # Lis une entrée de l'utilisateur depuis le clavier (fonction input), convertie en entier.
        n = int(input())
        # Condition de sortie : si l'utilisateur entre "0", on quitte la boucle et donc le programme.
        if n == 0:
            break
        else:
            # Sinon, on calcule et affiche la taille de l'intervalle premier contenant 'n'.
            print(length_of_gap_containing(n))

# Ceci permet de s'assurer que la fonction main() n'est exécutée que si ce fichier est lancé comme programme principal,
# et non s'il est importé comme module dans un autre programme.
if __name__ == '__main__':
    main()