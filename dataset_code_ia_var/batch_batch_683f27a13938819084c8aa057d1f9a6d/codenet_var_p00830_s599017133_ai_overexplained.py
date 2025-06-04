# Définition de la fonction `testcase_ends` qui traite un jeu de test
def testcase_ends():
    # Lecture de deux entiers depuis l'entrée standard, les convertissant en entiers à la volée
    # `n` représente le nombre de fichiers HTML, `m` le nombre de requêtes à traiter
    n, m = map(int, input().split())
    # Si les deux entiers lus valent 0, cela signifie que nous avons atteint la fin des données
    if (n, m) == (0, 0):
        return 1  # On retourne 1 pour signaler au programme principal qu'il faut arrêter

    # Création d'un set `htmls` contenant tous les chemins HTML donnés en entrée
    # Cela permet d'avoir une liste sans doublons et d'effectuer des recherches rapides
    htmls = set(input() for i in range(n))
    # Création d'un set `files` qui contient initialement uniquement la racine '/'
    files = set('/')
    # Pour chaque chemin HTML reçu en entrée
    for html in htmls:
        # On sépare le chemin en différents morceaux en utilisant le caractère '/' comme séparateur
        sp = html.split('/')
        # On ajoute dans `files` chaque dossier parent du fichier
        # La boucle commence à 2 pour éviter d'ajouter la racine vide
        for i in range(2, len(sp)):
            # On reforme le chemin jusqu'à l'élément d'indice i, puis on ajoute un '/' à la fin pour bien marquer que c'est un dossier
            files.add('/'.join(sp[:i]) + '/')
        # On ajoute enfin le chemin HTML complet dans la liste des fichiers
        files.add(html)

    # Définition de la fonction `find` qui va tenter de résoudre un chemin donné
    def find(url):
        # On vérifie si l'URL se termine déjà par un '/' (typiquement un dossier)
        has_ts = url.endswith('/')
        # On enlève tous les '/' finaux pour faciliter la gestion des noms et éviter des chaînes vides
        url = url.rstrip('/')
        # On divise le chemin en morceaux, l'élément de gauche étant vide car les chemins commencent par '/'
        sp = url.split('/')[1:]
        # La variable `u` va contenir le chemin courant en cours de reconstruction sous forme de liste
        # On commence avec la racine '' (car les chemins commencés par '/' sont vides avant le premier '/')
        u = ['']
        # On parcourt chacune des parties du chemin avec leur indice (on démarre à 1 car la racine est déjà ajoutée)
        for i, c in enumerate(sp, 1):
            # Si le morceau vaut '..' cela veut dire qu'il faut remonter d'un dossier (cas des chemins relatifs)
            if c == '..':
                # Si `u` est déjà vide, on ne peut pas remonter plus haut que la racine, donc chemin invalide
                if len(u) == 0:
                    return None  # Chemin inexistant
                # Sinon, on enlève le dernier dossier ajouté, ce qui correspond à remonter
                u.pop()
            # Si le morceau vaut '.' cela veut dire qu'on reste dans le même dossier (on ignore donc ce morceau)
            elif c == '.':
                pass  # Rien à faire dans ce cas
            else:
                # Sinon, on ajoute le dossier/fichier à la suite du chemin courant
                u.append(c)
            # On regarde si le chemin courant existe comme dossier (il doit se terminer par un '/')
            if ('/'.join(u) + '/') not in files:
                # Si celui-ci n'existe pas et qu'on n'est pas au bout du chemin, alors le chemin final sera forcément invalide
                if i < len(sp):
                    return None  # Chemin impossible, arrêt anticipé
        else:
            # À la fin, on recompose `u` en une chaîne séparée par des '/' pour obtenir le chemin complet
            u = '/'.join(u)

        # Si ce chemin complet se termine par '/' et qu'il existe un fichier 'index.html' à cet endroit
        if u.endswith('/') and (u+'index.html') in files:
            return u+'index.html'  # On retourne le fichier d'index
        # Si le chemin sans slash final mais en ajoutant '/index.html' existe, pareil
        if (u+'/index.html') in files:
            return u+'/index.html'
        # Si le chemin lui-même correspond à un fichier existant et qu'on n'a pas de slash terminal
        if u in files and not has_ts:
            return u  # On retourne le chemin du fichier directement

        # Sinon, le chemin ne correspond à rien d'existant
        return None

    # Pour chaque requête à traiter (il y en a `m`)
    for i in range(m):
        # On lit les deux chemins à comparer
        p1 = input()
        p2 = input()

        # On résout chaque chemin via la fonction `find`
        p1 = find(p1)
        p2 = find(p2)

        # Si au moins un des deux chemins n'existe pas après résolution, on affiche 'not found'
        if p1 is None or p2 is None:
            print('not found')
        # Si les deux chemins pointent vers le même fichier après résolution, on affiche 'yes'
        elif p1 == p2:
            print('yes')
        # Sinon, les deux chemins existent mais ne pointent pas vers le même fichier, on affiche 'no'
        else:
            print('no')

# Fonction principale qui boucle sur les jeux de test
def main():
    # On exécute la fonction `testcase_ends` tant qu'elle retourne 0 (ce qui veut dire qu'il reste des tests à faire)
    while not testcase_ends():
        pass  # Rien à faire ici, on continue simplement les tests

# Cette condition vérifie si le fichier est exécuté comme programme principal
if __name__ == '__main__':
    main()