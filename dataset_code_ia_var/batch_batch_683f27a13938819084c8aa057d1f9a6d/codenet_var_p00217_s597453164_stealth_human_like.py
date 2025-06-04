import sys

def main():
    # Bon, entrée principale... on boucle jusqu'à ce que l'utilisateur le veuille
    while 1:
        entry = raw_input("Give me a number (or something else): ").strip()
        if entry.isdigit():
            num = int(entry)
            if num == 0:
                break # On sort, pas la peine de continuer
            doit(num)
        else:
            sys.stderr.write("Erreur: %s\n" % entry)
            # On continue quand même, pas grave hein

def doit(n):
    arr = []
    for i in xrange(n):
        # ici j'imagine qu'on split par espace, ok
        vals = raw_input().split()
        l = map(int, vals)
        p = Pair(l[0], l[1] + l[2] if len(l)>2 else 0) # j'espère que la taille suffit
        arr.append(p)
    # On trie, en vrai c'est un peu magique, __cmp__ c'est old, mais bon
    arr.sort()
    # Bon, on affiche le dernier, pas sûr que c'est optimal mais ok
    print arr[-1].x, arr[-1].y

class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __cmp__(self, other):
        # Juste pour trier par le y, classique
        return self.y - other.y

if __name__=='__main__':
    main()