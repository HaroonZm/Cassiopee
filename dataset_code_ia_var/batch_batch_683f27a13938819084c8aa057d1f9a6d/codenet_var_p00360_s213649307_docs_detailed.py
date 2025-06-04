from bisect import bisect_left as bl

def main():
    """
    Lit une chaîne de caractères et un entier k, puis supprime au maximum k caractères de la chaîne initiale
    de façon à obtenir le plus petit mot possible par ordre lexicographique.
    Affiche le résultat à la fin.
    """
    # Entrée utilisateur : le mot à traiter, converti en une liste d'entiers (codes ASCII)
    s = list(map(ord, list(input())))
    # Entrée utilisateur : nombre maximal de suppressions autorisées
    k = int(input())
    
    # Liste des caractères déjà utilisés dans la solution finale (en code ASCII)
    used = []
    # Liste des indices (dans la chaîne initiale) des caractères déjà utilisés pour construire la solution
    used_index = []
    # Dictionnaire qui mappe chaque code ASCII à la liste de ses positions dans la chaîne (indices)
    pos_dict = {}
    as_a = ord("a")
    as_z = ord("z")
    
    # Remplit le dictionnaire avec les positions de chaque lettre dans la chaîne s
    for i, v in enumerate(s):
        if v in pos_dict:
            pos_dict[v].append(i)
        else:
            pos_dict[v] = [i]
    
    # Trie les lettres qui apparaissent dans la chaîne selon leur valeur ASCII (pour balayer les plus petites d'abord)
    keys = sorted(pos_dict.keys())
    # Pour chaque lettre, inverse la liste de positions pour pouvoir utiliser .pop() sur la dernière (la plus tôt)
    for key in keys:
        pos_dict[key].reverse()
    
    # Boucle principale : tant qu'il est possible de retirer au total <= k caractères
    while k:
        for key in keys:
            # 'init' : index dans la chaîne s de la prochaine occurrence de la lettre 'key' la plus tôt disponible
            init = pos_dict[key][-1]
            
            # 'pre_used' : combien de lettres déjà utilisées sont avant cette position init ?
            pre_used = bl(used_index, init)
            # Coût réel : nombre de suppressions nécessaires pour rendre ce caractère adjacent aux lettres déjà choisies
            cost = init - pre_used
            
            if cost <= k:
                # On a assez de "budget" k pour selectionner cette lettre à cette position
                k -= cost
                # Ajoute le caractère (code ASCII) à la solution
                used.append(key)
                # Ajoute son indice dans la liste triée used_index (insertion triée pour garder l'ordre croissant)
                ins = bl(used_index, init)
                used_index.insert(ins, init)
                # Retire cette occurrence de la lettre de la liste de positions
                pos_dict[key].pop()
                # Si plus aucune occurrence de cette lettre, l'enlever de la liste keys pour les prochaines itérations
                if not pos_dict[key]:
                    keys.remove(key)
                break # repart de la plus petite lettre
        else:
            # Si aucune suppression additionnelle n'est possible (plus de budget k ou plus de lettres disponibles)
            break
    
    # Trie les indices utilisés à l'envers pour ne pas fausser les indices lors des suppressions dans s
    used_index.sort(reverse=True)
    for i in used_index:
        s.pop(i) # Retire ces lettres de l'entrée initiale
    
    # La solution est la concaténation des lettres sélectionnées dans l'ordre optimal, suivies du reste de s
    print("".join(map(chr, used + s)))

if __name__ == "__main__":
    main()