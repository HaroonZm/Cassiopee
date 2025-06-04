def main():
    """
    Point d'entrée principale du programme.
    Ce programme prend des entrées de l'utilisateur sous la forme de deux chaînes séparées par un espace :
    - Une chaîne 's' représentant une séquence éventuellement compressée avec des répétitions et des parenthèses.
    - Un entier 'n' indiquant l'index recherché.
    Pour chaque paire entrée, le programme affiche le (n+1)-ième caractère de la chaîne décompressée, 
    ou 0 si cet indice n'existe pas.
    Termine lorsque l'utilisateur entre "0 0".
    """

    def pearser(s, n):
        """
        Décompresse récursivement une sous-chaîne donnée selon le schéma :
        Un nombre peut précéder une parenthèse ou un caractère, auquel cas le caractère ou 
        la séquence entre parenthèses est répété ce nombre de fois.
        Exemple : "3(a)" devient "aaa", "2(ab)" devient "abab".
        Fonction récursive qui reconstruit les n premiers caractères de la chaîne décompressée.

        Args:
            s (str): Segment de chaîne compressée à décoder.
            n (int): Nombre maximal de caractères à retourner.

        Returns:
            str: Les n premiers caractères de la chaîne décompressée.
        """
        if s == "":
            return ""  # Cas de base : chaîne vide, rien à décoder

        i = 0
        # Cherche un éventuel nombre en préfixe de la sous-chaîne
        while 1:
            if not s[i].isdigit():
                break
            i += 1

        if i == 0:
            # Pas de nombre en préfixe : on conserve le premier caractère tel quel
            r = pearser(s[i + 1:], n - 1)
            return s[0] + r
        # Si le caractère suivant est une parenthèse ouvrante, 
        # on traite la séquence entre parenthèses avec répétitions
        if s[i] == "(":
            r = Parentp(s[i:], n, int(s[:i]))
        else:
            # Sinon, on répète le caractère seul autant de fois que le nombre indiqué
            r = s[i] * int(s[:i])
            if len(r) >= n:
                return r[:n]
            # On concatène avec la suite décompressée, en veillant à la longueur n
            r += pearser(s[i+1:], n - len(r))
        return r

    def Parentp(s, n, p):
        """
        Décompresse une séquence de la forme "(...)" précédée d'un multiplicateur.
        Traite le bloc parenthésé, le décompresse, puis le répète p fois, 
        puis traite la suite éventuelle de la chaîne.

        Args:
            s (str): Séquence commençant par une parenthèse ouvrante '('.
            n (int): Nombre maximal de caractères à retourner au total.
            p (int): Nombre de répétitions du bloc entouré par les parenthèses.

        Returns:
            str: Les n premiers caractères de la composition décompressée.
        """
        if s == "":
            return ""  # Cas de base
        b = 0     # Indice du début du bloc parenthésé (juste après '(')
        c = 0     # Compteur de parenthèses pour repérer la fermeture
        i = 0
        # Recherche du bloc parenthésé complet (gestion de l'imbrication éventuelle)
        while 1:
            if s[i] == "(":
                c += 1
            if s[i] == ")":
                c -= 1
            if c == 0:
                break
            i += 1
        # Décompresse le contenu à l'intérieur des parenthèses
        r = pearser(s[b + 1:i], n)
        l = len(r)
        # Si le nombre total de caractères répétés dépasse n : on coupe à n caractères
        if l * p >= n:
            r = r * (n // l + 1)
            return r[:n]
        # Sinon, on répète et traite la suite, toujours à concurrence de n caractères
        r = r * p
        r += pearser(s[i+1:], n - len(r))
        return r

    def m(s, n):
        """
        Fonction de gestion de chaque requête utilisateur : 
        décompresse la chaîne et affiche le caractère à l'indice n,
        ou 0 si l'indice est trop grand.

        Args:
            s (str): Chaîne compressée saisie par l'utilisateur.
            n (str/int): Indice de position voulu (dans la chaîne décompressée).
        """
        n = int(n)
        # Décompression jusqu'à l'indice n inclus (pour vérifier si le n+1ème existe)
        r = pearser(s, n + 1)
        if len(r) <= n:
            print(0)
            return
        print(r[n])

    # Boucle principale d'interaction utilisateur
    while 1:
        s, n = map(str, input().split())
        if s == n == "0":
            break
        m(s, n)

main()