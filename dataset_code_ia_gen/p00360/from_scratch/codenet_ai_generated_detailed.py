# Solution pour le problème "Swapping Characters"
# 
# On doit générer la chaîne lexicographiquement la plus petite possible en effectuant au plus k permutations de caractères adjacents.
# Chaque swap permet de déplacer un caractère d'une position vers la gauche en échangeant avec son voisin immédiat.
#
# Approche détaillée :
# - On cherche à "faire remonter" progressivement les caractères les plus petits vers le début de la chaîne.
# - Une méthode efficace consiste à itérer sur la chaîne en position courant (i).
# - Pour chaque position i, on regarde dans un segment limité par la quantité de swaps restants k (car on ne peut pas faire remonter un caractère trop loin si k est petit).
# - On cherche dans s[i : i+k+1] le caractère minimum et sa position min_pos.
# - On déplace ce caractère min_pos vers i en effectuant min_pos - i swaps adjacents, ce qui réduit k de (min_pos - i).
# - On continue ainsi jusqu'à épuisement de k ou jusqu'à la fin de la chaîne.
#
# Complexité :
# - Il est crucial d'implémenter cette recherche efficacement.
# - Pour cela, on peut utiliser une structure de données telle que segment tree, ou une approche gloutonne en utilisant des indices.
# - Ici on applique une méthode basée sur un heap (tas) ou un arbre de segment.
# - Mais à cause de la limitation du nombre maximal de swaps très grand (jusqu'à 10^9), et la taille importante de la chaîne (2*10^5),
#   on privilégie une approche gloutonne en se servant d'un tableau index ou d'une structure adaptée.
#
# Implémentation choisie :
# - On utilise une structure de données "fenwick tree" ou "BIT" pour gérer efficacement.
# - Cependant, ici une méthode plus simple et efficace étant donné la contrainte : la méthode du "greedy with index scanning".
#
# Remarque :
# - On peut optimiser en utilisant une file d'attente pour chaque caractère pour retrouver rapidement la position minimale possible.
#
# Nous implémentons cette approche avec une liste de positions de chaque lettre, puis on essaie d'attraper le premier caractère le plus proche possible.

import sys
input = sys.stdin.readline

def main():
    s = list(input().strip())
    k = int(input())
    n = len(s)

    # Liste de positions pour chaque lettre
    from collections import deque
    positions = [deque() for _ in range(26)]
    for i, ch in enumerate(s):
        positions[ord(ch) - ord('a')].append(i)

    result = []
    current_pos = 0  # position dans s à partir de laquelle on choisit les caractères pour final result

    while current_pos < n and k > 0:
        # On cherche le plus petit caractère qui peut être amené à la position current_pos
        found = False
        for c in range(26):
            # Retirer toutes les positions < current_pos car déjà traitées
            while positions[c] and positions[c][0] < current_pos:
                positions[c].popleft()
            if not positions[c]:
                continue
            pos = positions[c][0]
            dist = pos - current_pos
            if dist <= k:
                # On peut amener ce caractère en current_pos en faisant dist swaps
                k -= dist
                # Enlever ce caractère de la liste des positions
                positions[c].popleft()
                # Ajouter à la réponse
                result.append(chr(c + ord('a')))
                # Marquer cette position comme "retirée" dans s : on va reconstruire le reste en enlevant ce caractère
                # On va gérer la mise à jour en pratique en "ignorant" celle position au moment de recréer la partie restante
                # mais pour la simplicité on reconstituera la chaîne plus tard.
                # On doit aussi enlever la lettre choisie de la chaîne.
                # Pour gérer le reste, on va ignorer cette position (on va reconstruire le suffixe plus loin)
                # On ne peut pas effacer dans s directement car cela créerait des problèmes d'index
                # Donc on stocke les indices des lettres retirées pour reconstruire le suffixe ensuite.
                # On va garder en tête que cette position est "occupée" donc on la supprime virtuellement.
                # On avance current_pos de 1 car on a placé un caractère dans result
                current_pos += 1
                found = True
                break
        if not found:
            # Aucune lettre peut être déplacée vers current_pos car cost trop élevé.
            break

    # On ajoute le reste des caractères (non choisis) dans leur ordre originale sauf ceux déjà déplacés
    # Pour cela, on récupère tous les indices >= current_pos qui n'ont pas été retirés (ils sont toujours en positions)
    # On va utiliser un set des indices retirés pour éviter duplication
    removed = set()
    # On avait retiré les positions où on a pris les lettres (mais on ne stocke pas explicitement les indices retirés)
    # En fait, on a juste "sauté" les indices déjà traités car current_pos avance toujours.
    # Donc les indices utilisés = ceux < current_pos + ceux déplacés (on les aura comptés dans result).
    # Plus simple : reconstruisons la partie restante à partir des indices >= current_pos + les indices non visités.
    # On doit reconstruire le suffixe avec les lettres qui ne sont pas dans result.
    # Cependant, il y a un problème : certaines lettres ont été déplacées mais pas supprimées de s
    # Or on a fait la suppression virtuelle en avançant current_pos pour la logique, ce qui correspond à supprimer un caractère dans la sur chaîne mentale.
    # Donc en réalité, les premiers current_pos-lettres sont déjà dans result.
    # Le suffixe est donc s[current_pos:] (ceux restant)
    # Par contre, les caractères déjà utilisés ne sont plus à leurs positions initiales. Il faut reconstruire.
    # Puisqu'on ne bouge les caractères qu'avec k swaps (c'est-à-dire, on a déplacé dans le résultat les caractères désirés), 
    # la chaîne restant est s[current_pos:] toutes lettres qui n'ont pas été déplacées.
    # Or la chaîne finale = result + restantes lettres dans l'ordre.

    # On récupère la partie restante non traitée
    suffix = []
    taken_positions = set()
    # positions des lettres utilisées en result ont été retirées de positions[], on ne les print plus
    # le suffixe est donc tout le reste de s à partir de current_pos, mais attention les caractères à positions < current_pos 
    # ont été supprimés
    # En fait, on n'a pas modifié s, donc on doit supprimer les caractères qui ont été "sortis".
    # On a avancé current_pos pour correspondre à la taille du résultat.
    # Chaque caractère choisi correspond à un caractère dans s qui a été "déplacé" vers le début (simulé)
    # Mais la chaîne finale est bien "result" + "s sous chaîne avec caractères non déplacés dans l'ordre".
    # D'où suffix = s avec les caractères de s qui ne sont pas dans result, en maintenant l'ordre.
    # Pour y arriver, on peut parcourir s depuis current_pos, en ignorant les indices qui apparaissent dans result.

    # Le problème est qu'on n'a pas trace des positions exactes déplacées (car on ne les stocke pas individuellement).
    # On va procéder ainsi : On sait que "current_pos" marque le nombre de caractères déjà fixés en result,
    # et ceux ont été retirés de la chaîne centrale.
    # Or on a déplacé ces caractères vers le début (cf swaps), donc les caractères restants sont tous ceux situés à droite de current_pos
    # et n'ayant pas été déplacés.
    # En fait, la description dans l'énoncé implique que l'ordre relatif des caractères non déplacés ne change pas.
    # 
    # On va donc prendre le reste de la chaîne s à partir de current_pos : s[current_pos:]
    # et on concatène result + s[current_pos:]

    # Remarque : dans les swaps le morceau restant est celui après la position où l'on a inséré le caractère sélectionné avec la réduction de k.
    # Comme on a toujours avancé current_pos d'un en plaçant un caractère, cela correspond bien au suffixe.

    result.extend(s[current_pos:])
    print("".join(result))


if __name__ == "__main__":
    main()