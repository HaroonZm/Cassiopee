# Boucle principale permettant de traiter plusieurs cas jusqu'à ce que l'entrée soit 0
while True:
    # Lecture du nombre d'éléments dans la définition des prix
    n = int(input())
    
    # Condition d'arrêt : si n est 0, on sort de la boucle
    if n == 0:
        break

    # Dictionnaire stockant les prix définis par défaut pour chaque article
    def_dic = {}

    # Lecture de n lignes composées d'un nom d'article et d'un prix,
    # puis insertion dans def_dic
    for _ in range(n):
        s, p = input().split()
        def_dic[s] = int(p)

    # Lecture du nombre de compositions décrivant comment certains articles sont fabriqués
    m = int(input())

    # Dictionnaire stockant pour chaque article les composants nécessaires à sa fabrication
    com_dic = {}

    # Lecture des m lignes contenant des informations sur les compositions :
    # La première valeur est l'article final, la troisième la liste des composants
    for _ in range(m):
        lst = input().split()
        # On considère que la syntaxe est {nom_article_final} = {composant1} {composant2} ...
        com_dic[lst[0]] = lst[2:]

    # Dictionnaire servant à mémoriser les prix calculés pour éviter les recalculs (mémoïsation)
    price_dic = {}

    def get_price(t):
        """
        Calcule le prix minimal pour obtenir l'article t.

        Si l'article t n'a pas de composition (pas dans com_dic),
        son prix est défini par def_dic.
        Sinon, on calcule le prix total des composants nécessaires pour fabriquer t,
        puis on retourne le minimum entre ce prix et le prix par défaut.

        La fonction utilise la mémoïsation via price_dic pour stocker les résultats
        déjà calculés afin d'optimiser les appels récursifs.
        
        Args:
            t (str): Nom de l'article dont on veut connaître le prix minimal.

        Returns:
            int: Prix minimal pour obtenir l'article t.
        """
        # Si le prix a déjà été calculé, on le retourne directement
        if t in price_dic:
            return price_dic[t]
        
        # Si l'article n'a pas de composition, on retourne son prix défini par défaut
        if t not in com_dic:
            price_dic[t] = def_dic[t]
            return def_dic[t]
        
        # Sinon, on calcule le coût total en sommant le prix de chaque composant
        x = 0
        for q in com_dic[t]:
            x += get_price(q)
        
        # Le prix final est le minimum entre le coût de la composition et le prix par défaut
        ret = min(x, def_dic[t])

        # On mémorise ce prix dans price_dic pour éviter de recalculer
        price_dic[t] = ret

        return ret

    # Lecture du nom d'article pour lequel on veut connaître le prix minimal,
    # puis affichage du résultat calculé par get_price
    print(get_price(input()))