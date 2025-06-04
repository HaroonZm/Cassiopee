import math

def process_input_line(line):
    """
    Traitement d'une ligne d'entrée, effectue les calculs nécessaires.

    Parameters:
        line (str): Ligne d'entrée contenant des entiers séparés par des espaces.

    Returns:
        str: "OK" si la condition est remplie, "NA" sinon.
    """
    # Conversion de la ligne d'entrée en liste d'entiers
    values = list(map(int, line.split()))
    # Le premier entier est 'l', le quota ou la limite principale
    l = values[0]
    # La liste 'r' contient tous les autres entiers à partir de l'indice 1
    r = values[1:]
    n = len(r)

    # Vérifie si le double de la somme des éléments de r est inférieur ou égal à l
    if 2 * sum(r) <= l:
        return "OK"

    # Sinon, on doit essayer de minimiser une grandeur dépendant de l'agencement des r
    s = []

    if n > 1:
        # Trie la liste r pour une organisation spécifique permettant de minimiser le calcul suivant
        r.sort()
        # Construction d'une nouvelle liste s en alternant éléments extrêmes de r
        for i in range(n // 2):
            # Ajoute l'élément en position i au début et celui en position -i-1 à la fin, retournant s pour équilibrer
            s = [r[i]] + s[::-1] + [r[-i-1]]
        if n & 1:
            # Si n est impair, il reste un élément central à insérer là où l'écart minimal avec s est atteint
            if abs(s[0] - r[n // 2]) < abs(s[-1] - r[n // 2]):
                s.append(r[n // 2])
            else:
                s = [r[n // 2]] + s
    else:
        # Cas particulier si r contient un seul élément
        s = r

    # Calcule la grandeur finale 'ans' à partir des éléments réordonnés dans s
    # On commence avec la somme du premier et du dernier élément
    ans = s[0] + s[-1]
    # On ajoute, pour chaque paire consécutive, deux fois la racine carrée de leur produit
    for i in range(n - 1):
        ans += 2 * math.sqrt(s[i] * s[i + 1])

    # Retourne "OK" si le résultat est inférieur à l (en tenant compte d'une petite marge d'erreur), "NA" sinon
    return "OK" if ans < 0.000000001 + l else "NA"

def main():
    """
    Boucle principale du programme. Lit les entrées standard ligne par ligne et affiche le résultat du traitement.
    """
    while True:
        try:
            # Lecture d'une ligne au clavier de façon compatible Python 2 (raw_input) et Python 3 (input)
            try:
                line = raw_input()
            except NameError:
                line = input()
        except EOFError:
            # Arrêt lorsqu'il n'y a plus de lignes à lire (fin de fichier)
            break

        # Ignore les lignes vides
        if not line.strip():
            continue

        # Traite la ligne lue et affiche le résultat
        result = process_input_line(line)
        print(result)

if __name__ == "__main__":
    main()