import random

def read_input():
    """
    Lit l'entrée utilisateur et renvoie le nombre d'éléments et le nombre cible.
    
    Returns:
        tuple: (N, X) où N est le nombre d'éléments (int),
               et X est le nombre cible (str, binaire).
    """
    N, X = input().split()
    N = int(N)
    return N, X

def read_vectors(N):
    """
    Lit N entiers binaires depuis l'entrée standard et les convertit en entiers.
    
    Args:
        N (int): Le nombre d'entiers à lire.
        
    Returns:
        list: Liste d'entiers.
    """
    A = []
    for i in range(N):
        A.append(int(input(), 2))
    return A

def build_basis(A, M, X):
    """
    Construit une base de l'espace vectoriel sur F2 à partir de la liste A.
    Elle prépare également des structures de données pour les opérations futures.
    
    Args:
        A (list): Liste triée des entiers.
        M (int): Longueur maximale des bits à traiter.
        X (str): Chaîne binaire cible.
        
    Returns:
        tuple: (data, data2), où
            data (list): Base du sous-espace sur F2 représentée par les entiers.
            data2 (list): Cumul des rangs partiels de la base.
    """
    data = [0] * (M + 1)  # Base initiale : tous les coefficients à zéro

    # Ajout du plus grand vecteur à la base
    a = A[-1]
    n = a.bit_length() - 1
    # Décale le vecteur de sommet pour initialisation
    for i in range(M - n, -1, -1):
        data[i + n] = a << i

    low = n  # Indique le plus petit bit du sommet de la base actuellement construit
    
    # Construction incrémentale de la base de Gauss sur F2
    for i in range(0, len(A) - 1):
        a = A[i]
        flag = True
        while flag:
            n = a.bit_length()
            # Réduit a par rapport à la base courante
            for j in range(n - 1, low - 1, -1):
                a = min(a, a ^ data[j])
            if a != 0:
                data[a.bit_length() - 1] = a
                id = a.bit_length() - 1
                low = id  # Met à jour la "hauteur" minimale de la base
                # Complète la base vers le haut par combinaisons linéaires
                while data[id + 1] == 0:
                    data[id + 1] = min((data[id] << 1) ^ a, (data[id] << 1))
                    id += 1
                else:
                    a = data[id] << 1
            else:
                break

    # Crée un tableau de booléens (0 ou 1) indiquant quels bits sont présents dans la base
    data2 = [0] * (M + 1)
    for i in range(M + 1):
        data2[i] = int(data[i] != 0)

    # Prend le cumul pour faciliter le calcul du rang partiel
    for i in range(1, M + 1):
        data2[i] += data2[i - 1]
    
    # Décale pour obtenir un indexage pratique lors du parcours
    data2 = [0] + data2

    return data, data2

def count_Xor_representations(data, data2, X, mod):
    """
    Compte le nombre de sous-ensembles de la base générant un XOR <= X (binaire).
    Utilise le calcul du nombre de solutions bornées dans une base de l'espace vectoriel sur F2.
    
    Args:
        data (list): Base de Gauss sur F2 des entiers initiaux.
        data2 (list): Rang cumulatif des bits de la base.
        X (str): Chaîne binaire cible (par exemple '10101').
        mod (int): Module pour éviter les débordements.
        
    Returns:
        int: Le nombre de sous-ensembles dont le XOR est <= X modulo 'mod'.
    """
    x = 0         # XOR courant lors du parcours de X
    ans = 0       # Compteur du résultat final
    n = len(X) - 1  # Indice du bit de plus haut poids dans X
    
    for i in range(len(X)):
        if X[i] == "1":
            # Cas où le bit courant dans x est aussi 1
            if (x >> (n - i)) & 1 == 1:
                if data[n - i]:
                    ans += pow(2, data2[n - i], mod)
                    ans %= mod
            else:
                ans += pow(2, data2[n - i], mod)
                ans %= mod
                if data[n - i]:
                    x = x ^ data[n - i]
                else:
                    break
        else:
            if (x >> (n - i)) & 1 == 1:
                if data[n - i]:
                    x = x ^ data[n - i]
                else:
                    break
            else:
                continue
    else:
        # Si toutes les contraintes sont satisfaites, on compte la représentation exacte
        ans += 1
        ans %= mod
    return ans

def main():
    """
    Fonction principale — exécute la logique de calcul du nombre de sous-ensembles XOR inférieurs ou égaux à X.
    """
    # Module pour éviter les débordements numériques lors des manipulations exponentielles
    mod = 998244353

    # Lecture de l'entrée et conversion des données binaires en entiers
    N, X = read_input()
    A = read_vectors(N)
    A.sort()  # Trie les éléments pour les traitements de base

    # Détermination du nombre maximal de bits à manipuler (entre X et le max de A)
    a = A[-1]
    M = max(len(X) - 1, a.bit_length() - 1)

    # Construction de la base et du rang partiel
    data, data2 = build_basis(A, M, X)

    # Calcul du nombre de sous-ensembles valides dont le XOR est <= X
    ans = count_Xor_representations(data, data2, X, mod)

    # Affichage du résultat final
    print(ans)

if __name__ == "__main__":
    main()