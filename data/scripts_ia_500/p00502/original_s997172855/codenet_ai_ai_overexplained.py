d,n=map(int,input().split())  
# On lit d et n à partir de l'entrée standard.  
# `input()` récupère la ligne sous forme de chaîne de caractères.  
# `split()` sépare cette chaîne en une liste de sous-chaînes selon les espaces.  
# `map(int, ...)` convertit chaque sous-chaîne en entier.  
# On déstructure ensuite le résultat en variables `d` et `n`.  
  
t=[int(input()) for _ in [0]*d]  
# On crée une liste `t` qui contient `d` éléments.  
# Pour chaque élément, on lit une ligne d'entrée contenant un entier.  
# L'expression `[0]*d` génère une liste de `d` zéros, juste pour itérer `d` fois.  
# La liste `t` contiendra donc `d` entiers lus ligne par ligne.  
  
abc=[list(map(int,input().split())) for _ in [0]*n]  
# De manière similaire, on crée une liste `abc` qui contient `n` sous-listes.  
# Chaque sous-liste est obtenue en lisant une ligne, en la découpant en sous-chaînes séparées par des espaces,  
# en convertissant chacune en entier, puis en transformant le résultat en liste.  
# Chaque élément de `abc` est donc une liste de trois entiers `[a, b, c]`.  
  
memo=[-1]*101  
# On initialise une liste `memo` de longueur 101 avec des valeurs par défaut à -1.  
# Chaque index de 0 à 100 correspond probablement à une valeur ou un état particulier.  
# La valeur -1 indique que cet état n'a pas encore été atteint ou calculé.  
  
t_list=[set() for _ in [0]*61]  
# On crée une liste `t_list` de 61 éléments, chaque élément étant un ensemble vide.  
# Le but est de représenter à chaque position (indexé de 0 à 60) un ensemble d'entiers associés.  
# L'utilisation d'un set garantit que les éléments sont uniques et permet des recherches rapides.  
  
for a,b,c in abc:  
    # On parcourt chaque triplet (a,b,c) dans la liste `abc`.  
    for j in range(a,b+1):  
        # Pour chaque entier j allant de a à b inclus,  
        t_list[j].add(c)  
        # On ajoute c dans le set correspondant à l'indice j de t_list.  
        # Cela signifie que l'élément c est "rattaché" à tous les indices entre a et b.  
  
for i in t_list[t[0]]:  
    # On regarde le premier élément de la liste `t` (c'est un entier entre 0 et 60 inclus, on suppose).  
    # On récupère le set d'entiers associés à cet indice dans t_list.  
    memo[i]=0  
    # On met à jour la liste `memo` : pour chaque entier i dans ce set, on initialise la valeur à 0.  
    # Cela signifie que ces états ou positions sont atteignables dès le départ, avec un coût ou score 0.  
  
for i in t[1:]:  
    # On itère sur la liste `t` à partir du deuxième élément jusqu'au dernier (index 1 à d-1).  
    memo2=[-1]*101  
    # Pour chaque itération, on crée une nouvelle liste `memo2` de taille 101 initialisée à -1,  
    # qui servira à stocker les meilleures valeurs possibles pour la nouvelle étape.  
    temp=[j for j in t_list[i]]  
    # On crée une liste `temp` qui contient tous les entiers présents dans le set t_list[i].  
    # Cela correspond aux états disponibles à la position i de t.  
  
    for j,k in enumerate(memo):  
        # On parcourt tous les indices j (de 0 à 100) et valeurs k (score associé) dans `memo`.  
        if k!=-1:  
            # On ne considère que les indices pour lesquels une valeur calculée existe (différente de -1).  
            for l in temp:  
                # Pour chaque état l dans la liste temp correspondant à la position i.  
                # On calcule la valeur potentielle en passant de l'état j à l'état l.  
                memo2[l]=max(memo2[l],k+abs(j-l))  
                # On met à jour memo2[l] : on prend la maximum entre l'ancienne valeur memo2[l] et la somme de k plus la distance absolue entre j et l.  
                # Cela correspond à accumuler un score basé sur la transition entre l'état précédent j et le nouvel état l.  
  
    memo=memo2  
    # On remplace la liste memo par la nouvelle liste memo2 préparée.  
    # Ainsi, pour l'étape suivante, on utilisera les valeurs calculées ici.  
  
print(max(memo))  
# Enfin, on affiche la valeur maximale présente dans la liste memo.  
# Cela correspond au score maximal atteint après toutes les étapes.  
# La fonction max prend en compte tous les 101 états possibles et retourne la plus grande valeur calculée.