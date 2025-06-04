# Définition de la fonction check qui prend un argument 'a'
def check(a):
    # Initialisation d'une liste vide 'path', qui stockera les parties du chemin traité
    path = []
    # Boucle sur chaque 'direct' obtenu en découpant la chaîne 'a' à partir du 2ème caractère (pour ignorer le premier caractère, généralement '/'),
    # puis en faisant un split sur le caractère '/', ce qui retourne une liste de sous-chaînes pour chaque répertoire ou fichier
    for direct in a[1:].split("/"):
        # Si la sous-chaîne est '.', cela signifie le répertoire courant donc on l'ignore et continue à la prochaine itération
        if   direct == ".": 
            continue
        # Si la sous-chaîne est chaîne vide (cela peut se produire à cause de deux '///' collés ou au début), on la remplace par '/', qui représente la racine
        elif direct == "" : 
            direct = "/"
        # Si la sous-chaîne est '..', cela signifie qu'on doit remonter d'un répertoire dans notre chemin logique
        elif direct == "..":
            # On vérifie si 'path' est vide (donc on est déjà à la racine), ou bien si aucun url existant correspondant au chemin actuel n'est trouvé dans la liste 'urls'
            # max(url.find(...)) renverra -1 si tout échoue, on vérifie alors cette condition
            if len(path) == 0 or max(url.find("/"+"/".join(path)+"/") for url in urls) == -1: 
                # Si impossible de remonter, on retourne False pour signifier une erreur
                return False
            # Sinon, on enlève le dernier élément de path, effectuant ainsi le "remonter d'un dossier"
            path.pop()
            # On saute le reste de l'itération et continue
            continue
        # Pour tous les autres cas (c'est un nom de dossier ou fichier normal), on l'ajoute à la liste path pour progresser dans la construction du chemin
        path.append(direct)
    # Après la boucle, on construit une chaîne url débutant par '/' et joignant tous les éléments (dossiers/fichier) de path par des '/'
    url = "/" + "/".join(path)
    # Corrige les cas ou plusieurs '/' se succèdent, en les remplaçant par un seul('/')
    while "//" in url: 
        url = url.replace("//","/")
    # On vérifie si cette url (chemin traité) existe dans la liste des urls connues, auquel cas on retourne aussitôt cette url
    if url in urls: 
        return url
    # Si ce n'est pas trouvé, on teste l'ajout final de "/index.html" (cas d'une url de type répertoire)
    # On corrige une nouvelle fois les doubles slashs au besoin
    url = (url + "/index.html").replace("//","/")
    # Si l'url finale après cette modification existe, on la retourne, sinon on retourne False
    return url if url in urls else False

# Boucle infinie principale pour traiter plusieurs jeux de données
while 1:
    # Lecture et découpage de la ligne utilisateur en deux entiers n et m, séparés par des espaces
    n, m = map(int, raw_input().split())
    # Si n vaut 0, cela signifie la fin des jeux de données, on quitte la boucle en utilisant break
    if n == 0: 
        break
    # Lecture des n urls suivantes et construction de la liste des urls
    urls = [raw_input() for i in xrange(n)]
    # Pour chaque test parmi les m à réaliser sur ce jeu de données
    for loop in xrange(m):
        # Lecture d'une première entrée utilisateur, traitement du chemin par la fonction check, résultat stocké dans 'a'
        a = check(raw_input())
        # Lecture d'une seconde entrée utilisateur, traitement du chemin également, résultat dans 'b'
        b = check(raw_input())
        # Si l'un des deux résultats retourne False (soit l'url n'existe pas, soit une erreur de cheminement), on imprime 'not found'
        if not (a and b): 
            print "not found"
        # Si les deux urls traitées existent, mais ne sont pas identiques (après normalisation), on imprime 'no'
        elif a != b: 
            print "no"
        # Si les deux urls traitées sont identiques, on imprime 'yes'
        else: 
            print "yes"