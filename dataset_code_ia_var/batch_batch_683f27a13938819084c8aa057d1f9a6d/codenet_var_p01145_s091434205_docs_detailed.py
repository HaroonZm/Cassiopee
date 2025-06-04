import sys

# Raccourcis pour les entrées/sorties
readline = sys.stdin.readline
write = sys.stdout.write

def gen(e, k):
    """
    Génère une chaîne de caractères à partir d'un tuple représentant une unité phonologique.

    Args:
        e (tuple): Un tuple de quatre éléments (cc, c0, c1, c2).
            - cc : consonne doublée (pour le sokuon, ex: 'k')
            - c0 : consonne ou groupe de consonnes (ex: 'k', 'ky', ...)
            - c1 : voyelle (ex: 'a', 'i', 'u', ...)
            - c2 : voyelle longue supplémentaire (ex: 'a', 'i', 'u' pour voyelle longue)
        k (int): Indicateur. Si k=1, parenthèse la voyelle pour une ambiguïté.

    Returns:
        str: La représentation sous forme de chaîne de l'unité phonologique.
    """
    r = []
    if e[0]:
        # Ajoute la consonne double (sokuon) si elle existe
        r.append(e[0])
    if e[1]:
        # Ajoute la consonne ou groupe consonne-voyelle principal
        r.append(e[1])
    if e[2]:
        # Ajoute la voyelle, éventuellement parenthésée
        if k:
            r.append("(" + e[2] + ")")
        else:
            r.append(e[2])
    if e[3]:
        # Ajoute la voyelle longue si elle existe
        r.append(e[3])
    return "".join(r)

def solve():
    """
    Lit une ligne d'entrée, la traite en tant que romanisation du japonais,
    divise la chaîne en unités phonologiques, puis réapplique des ajustements pour
    gérer les ambiguïtés de segmentation, et affiche la chaîne transformée.

    Returns:
        bool: False si l'entrée est le caractère de fin '#', True sinon.
    """
    s = readline().strip()
    if s == '#':
        return False

    # Voyelles et consonnes japonaises possibles en romanisation
    vs = "aiueo"       # voyelles
    cs = "kstnhmyrwgzdbp"  # consonnes

    t = []   # Liste des unités phonologiques extraites
    L = len(s)
    i = 0
    while i < L:
        c0 = s[i]
        if c0 in cs:
            cc = None  # Pour éventuelle consonne doublée (sokuon)
            if c0 == 'n':
                # Cas du ん (n) indépendant ou suivi d'une apostrophe
                if i == L - 1:
                    t.append((None, "n", None, None))
                    i += 1
                    continue
                c1 = s[i + 1]
                if c1 == "'":
                    t.append((None, "n'", None, None))
                    i += 2
                    continue
                if c1 in cs and c1 != 'y':
                    t.append((None, "n", None, None))
                    i += 1
                    continue
            c1 = s[i + 1]  # Recherche du potentiel suivant

            # Gestion du sokuon (っ), consonne doublée
            if c1 in cs and c1 not in "nyw":
                cc = c0
                c0 = c1
                i += 1
                c1 = s[i + 1]

            # Gestion du yôon (ky, sy, ty, etc)
            if c1 == 'y':
                c0 += c1
                i += 1
                c1 = s[i + 1]

            # Vérifie que la prochaine lettre est bien une voyelle
            assert c1 in vs, (cc, c0, c1)
            # Gestion de la voyelle longue (chôon)
            if i + 1 < L - 1:
                c2 = s[i + 2]
                if c2 in "aiu":
                    i += 3
                    t.append((cc, c0, c1, c2))
                    continue
            t.append((cc, c0, c1, None))
            i += 2
        else:
            # Cas où la lettre n'est pas une consonne (donc une voyelle ou autre)
            if i < L - 1:
                c1 = s[i + 1]
                if c1 in "aiu":
                    i += 2
                    t.append((None, None, c0, c1))
                    continue
            t.append((None, None, c0, None))
            i += 1

    # Groupes pouvant provoquer une ambiguïté lors de la segmentation
    ps = ["k", "s", "t", "h", "p", "ky", "sy", "ty", "hy", "py"]
    i = 0
    L = len(t)
    ans = []   # Stocke le résultat final

    while i < L:
        a0, b0, c0, d0 = t0 = t[i]
        i += 1

        if b0 not in ps:
            # Pas d'ambiguïté, ajout normal
            ans.append(gen(t0, 0))
            continue

        if i == L:
            # Dernière unité, vérifie si parenthésage requis pour l'ambiguïté
            if b0 in ps and c0 in "iu" and d0 is None:
                ans.append(gen(t0, 1))
                continue
        else:
            a1, b1, c1, d1 = t1 = t[i]
            if b1 in ps:
                # Si deux groupes ambigus se suivent
                if c0 in "ao" and c0 == c1:
                    if d0 is None and a1 is None:
                        ans.append(gen(t0, 1))
                        ans.append(gen(t1, 0))
                        i += 1
                        continue
                if c0 in "iu" and d0 is None:
                    ans.append(gen(t0, 1))
                    ans.append(gen(t1, 0))
                    i += 1
                    continue
        ans.append(gen(t0, 0))
    # Affiche la ligne transformée
    write("".join(ans))
    write("\n")
    return True

# Boucle principale : traite les entrées ligne par ligne jusqu'à rencontre de '#'
while solve():
    ...