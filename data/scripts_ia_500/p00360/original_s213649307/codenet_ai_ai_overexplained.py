from bisect import bisect_left as bl  # Importation de la fonction bisect_left du module bisect, renommée en 'bl' pour faciliter son utilisation dans le code. Cette fonction sert à trouver l'indice où insérer un élément dans une liste triée pour maintenir l'ordre.

def main():
    # Lecture de la chaîne de caractères entrée par l'utilisateur
    # La chaîne est convertie en liste de caractères, puis chaque caractère est transformé en son code ASCII via la fonction ord
    # On obtient ainsi une liste d'entiers représentant les caractères de la chaîne
    s = list(map(ord, list(input())))
    
    # Lecture de l'entier k fourni par l'utilisateur, on convertit l'entrée textuelle en entier avec int()
    k = int(input())
    
    # Initialisation d'une liste vide pour stocker les caractères utilisés dans la nouvelle chaîne finale
    # Ces caractères sont stockés sous forme de leur code ASCII
    used = []
    
    # Initialisation d'une autre liste vide pour garder la trace des indices des caractères originaux qui ont été utilisés
    used_index = []
    
    # Initialisation d'un dictionnaire vide nommé pos_dict
    # Ce dictionnaire aura pour clé la valeur ASCII d'un caractère
    # Sa valeur associée sera la liste des positions (indices) dans la chaîne originale où ce caractère apparaît
    pos_dict = {}
    
    # Variables pour les codes ASCII de 'a' et 'z', utilisées pour possiblement faciliter d'autres opérations ou comparaisons
    as_a = ord("a")
    as_z = ord("z")
    
    # Parcours de tous les caractères (code ASCII) de la chaîne, avec leur position respective
    for i, v in enumerate(s):
        # Si le caractère (code ASCII) est déjà une clé du dictionnaire pos_dict
        if v in pos_dict:
            # On ajoute la position i à la liste des positions correspondant à ce caractère
            pos_dict[v].append(i)
        else:
            # Si le caractère n'était pas encore une clé du dictionnaire, on crée une nouvelle entrée avec une liste contenant la position i
            pos_dict[v] = [i]
    
    # Récupération de la liste des clés du dictionnaire (tous les caractères uniques sous forme de code ASCII)
    # Triée dans l'ordre croissant (donc de 'a' vers 'z') pour traiter les caractères dans l'ordre alphabétique
    keys = sorted(pos_dict.keys())
    
    # Pour chaque ensemble de positions associées à un caractère, on inverse la liste
    # Cela facilite la récupération de la dernière occurrence d'un caractère via la méthode pop(), qui est plus efficace sur la fin de la liste
    for key in keys:
        pos_dict[key].reverse()
    
    # Tant que le nombre k (qui représente un "budget" ou "coût" maximal autorisé) est strictement supérieur à 0 on continue
    while k:
        # Pour chaque caractère (dans l'ordre alphabétique) on essaie de voir s'il peut être ajouté à la solution en respectant le budget k
        for key in keys:
            # On récupère la dernière position possible du caractère courant, qui est la position la plus récente dans la liste inversée
            init = pos_dict[key][-1]
            
            # La variable pre_used est obtenue en cherchant l'endroit (via bisect_left) où la position init devrait être insérée dans la liste des indices déjà utilisés (qui est triée)
            # Cela correspond au nombre d'indices déjà utilisés qui sont inférieurs à init
            pre_used = bl(used_index, init)
            
            # Le coût pour récupérer ce caractère est calculé dans la variable cost, égale à la position init moins le nombre d'indices déjà utilisés avant init
            # Ce calcul semble modéliser la distance corrigée par les suppressions déjà effectuées
            cost = init - pre_used
            
            # Si ce coût est inférieur ou égal au budget k restant, on accepte ce caractère
            if cost <= k:
                # On décrémente k du coût associé à ce caractère
                k -= cost
                
                # On ajoute le caractère (code ASCII) dans la liste des caractères utilisés
                used.append(key)
                
                # On calcule la position où insérer la position init dans la liste triée used_index afin de garder la liste triée
                ins = bl(used_index, init)
                
                # On insère cette position à son endroit correct dans used_index
                used_index.insert(ins, init)
                
                # On retire la position utilisée de la liste des positions du caractère concerné via pop()
                pos_dict[key].pop()
                
                # Si après cette opération la liste des positions de ce caractère est vide, on enlève le caractère des clés utilisées (car il ne reste plus d'occurence à traiter)
                if not pos_dict[key]:
                    keys.remove(key)
                
                # On sort de la boucle des caractères pour passer au prochain tour du while, car on a effectué une suppression/retrait
                break
        else:
            # Si on termine la boucle for sans faire de break, cela signifie qu'aucun caractère ne peut être ajouté selon le budget restant
            # On sort donc de la boucle while principale
            break
    
    # Tri de la liste des indices utilisés en ordre décroissant (du plus grand au plus petit)
    # Ceci facilite la suppression des caractères à ces indices dans la liste originale puisque supprimer à partir de la fin ne modifie pas les indices des caractères précédents
    used_index.sort(reverse=True)
    
    # Suppression des caractères originaux dans la liste s aux positions indiquées dans used_index
    for i in used_index:
        s.pop(i)
    
    # Reconstruction et affichage de la chaîne finale
    # On convertit d'abord chaque code ASCII dans la liste used en caractères avec chr
    # Puis, on concatène cette liste (de caractères choisis) avec la liste modifiée s (charset restant après suppressions)
    # Enfin, on joint tout en une chaîne de caractères et on affiche avec print
    print("".join(map(chr, used + s)))

# Appel de la fonction principale pour lancer l'exécution du programme
main()