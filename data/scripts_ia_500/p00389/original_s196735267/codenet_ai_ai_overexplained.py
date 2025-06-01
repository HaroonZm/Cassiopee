# On commence par lire une ligne d'entrée utilisateur qui contient deux nombres entiers séparés par un espace.
# La fonction input() permet de lire une chaîne de caractères depuis l'entrée standard (le clavier).
# La méthode split() divise cette chaîne en une liste de sous-chaînes en utilisant l'espace par défaut comme séparateur.
# La fonction map() applique la fonction int à chacun des éléments de cette liste pour les convertir en entiers.
# On affecte ensuite ces deux entiers aux variables n et k, respectivement.
n, k = map(int, input().split())

# Initialisation de la variable 'ans' qui va compter le nombre de fois que la condition dans la boucle est satisfaite.
ans = 0

# Initialisation de deux variables 'd' et 's' (probablement représentant une sorte de division et somme dans ce contexte).
# 'd' est initialisé à 1, représentant possiblement un diviseur ou un compteur.
# 's' est initialisé à 0, représentant une somme cumulative.
d, s = 1, 0

# Début d'une boucle infinie. Cette boucle va continuer tant qu'on ne rencontre pas un break.
while True:
    # Commentaire expliquant une condition mathématique liée aux variables s, d et k.
    # La condition s/d <= k peut être réarrangée en s <= d*k.
    # Pour maintenir cette relation, on ajuste 'd' pour que d*k soit au moins égal à s.
    
    # Tant que la condition d*k < s est vraie, on augmente 'd' de 1.
    # Cela garantit que d*k sera toujours supérieur ou égal à s à la sortie de cette boucle.
    while d * k < s:
        d += 1
    
    # Ici, on vérifie si la somme actuelle 's' plus la valeur 'd' dépasse la limite 'n'.
    # Si c'est le cas, on quitte la boucle infinie avec break.
    if s + d > n:
        break
    
    # Sinon, on ajoute 'd' à la somme 's'.
    s += d
    
    # On incrémente le compteur 'ans' de 1 car une unité valide a été comptabilisée.
    ans += 1

# Après la sortie de la boucle, on affiche la valeur finale de 'ans'.
# La fonction print() convertit l'entier en chaîne et l'affiche sur la sortie standard (écran).
print(ans)