import sys

def can_layout(words, W, max_spaces):
    """
    Vérifie si on peut organiser les mots en lignes de largeur W,
    avec un maximum de max_spaces espaces consécutifs entre deux mots.
    
    Cette fonction simule le placement des mots ligne par ligne en respectant la contrainte max_spaces.
    """
    n = len(words)
    idx = 0  # index du mot courant
    while idx < n:
        line_len = 0  # longueur cumulée sur la ligne courante
        # On place au moins un mot sur la ligne
        line_len += words[idx]
        idx += 1
        # Tenter d'ajouter d'autres mots au même ligne tant que cela reste possible
        while idx < n:
            # ajouter au minimum un espace
            # entre les mots, on doit placer au moins un espace et au plus max_spaces
            # On prendra max_spaces espaces pour que la justification soit possible
            # mais on vérifie juste que la ligne ne dépasse pas W
            # En réalité, pour vérifier la possibilité, on suppose que
            # entre les mots il y a exactement max_spaces espaces.
            sep = max_spaces
            if line_len + sep + words[idx] > W:
                break
            line_len += sep + words[idx]
            idx += 1
        # Après placement, la ligne doit commencer à la colonne 1 (idx 0)
        # et se finir exactement à W (sans espaces superflus à la fin)
        # Ici on a simulé avec max_spaces espaces entre les mots sauf la dernière ligne que nous ne
        # connaissons pas encore.
        # En can_layout on doit juste vérifier que placement est possible.
        if line_len > W:
            return False
    return True

def find_min_max_space(words, W):
    """
    Recherche la plus petite valeur possible pour le plus long espace contigu
    entre les mots dans la disposition du texte.
    """
    # La borne inférieure minimale est 1 espace
    low = 1
    # La borne supérieure maximale est W (au cas extrême tous les espaces réunis)
    high = W
    result = W

    while low <= high:
        mid = (low + high) // 2
        if can_layout(words, W, mid):
            # Si on peut avec cette valeur max d'espaces contigus, on la cherche plus petite encore
            result = mid
            high = mid - 1
        else:
            # Sinon on doit augmenter le max d'espaces permis
            low = mid + 1

    return result

def main():
    input = sys.stdin.read().strip().split()
    pos = 0
    while True:
        if pos >= len(input):
            break
        W = int(input[pos]); pos+=1
        N = int(input[pos]); pos+=1
        if W == 0 and N == 0:
            break
        words = list(map(int, input[pos:pos+N]))
        pos += N

        # Trouver et afficher la plus petite valeur possible du plus long espace contigu
        res = find_min_max_space(words, W)
        print(res)

if __name__ == '__main__':
    main()