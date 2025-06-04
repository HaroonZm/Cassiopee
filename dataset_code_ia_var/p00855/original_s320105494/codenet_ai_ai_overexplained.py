import sys         # Importe le module sys pour lire les entrées via stdin
import bisect      # Importe le module bisect pour rechercher efficacement dans une liste triée

MAX = 1299710      # Définit la variable MAX à 1299710, correspondant à la limite supérieure des nombres premiers à considérer

# Crée une liste nommée 'prime' avec MAX éléments, initialisés à -1
# On utilisera cette liste pour savoir si un nombre est premier ou non :
#   -1  : non encore évalué
#    0  : nombre premier
#    1  : non premier
prime = [-1] * MAX

prime_list = []    # Initialise une liste vide pour stocker tous les nombres premiers trouvés

i = 2              # Commence le criblage à partir de 2, le plus petit nombre premier

# Boucle pour remplir la liste des nombres premiers jusqu'à la valeur MAX (non incluse)
while MAX > i:                     # Tant que i est strictement inférieur à MAX
    if prime[i - 1] == -1:         # Si le (i-1)ème index vaut -1, alors i n'a pas encore été traité
        prime[i - 1] = 0           # Marque i comme premier en mettant 0 à la position (i-1)
        temp = i * 2               # Initialise temp à 2 fois i, pour parcourir les multiples de i
        prime_list.append(i)       # Ajoute le nombre premier trouvé à 'prime_list'
        # Remplit la liste 'prime' en marquant tous les multiples de i comme non premiers
        while temp < MAX:          # Pour chaque multiple de i inférieur à MAX
            prime[temp - 1] = 1    # Marque ce multiple (temp) comme non premier en mettant 1 à (temp-1)
            temp += i              # Passe au prochain multiple de i
    if i == 2:                     # Si i vaut 2 (le cas particulier du seul nombre pair premier)
        i += 1                     # Passe à 3, le prochain nombre premier
    else:
        i += 2                     # Incrémentation de 2 pour ne vérifier que les entiers impairs (sauf 2 déjà traité)

# Début d'une boucle infinie pour traiter les entrées utilisateur
while True:
    n = int(sys.stdin.readline())   # Lit une ligne depuis l'entrée standard, la convertit en entier et la stocke dans n

    if n == 0:                     # Condition de sortie de la boucle : si la valeur lue est 0, on arrête le programme
        break

    # Cherche la position où n pourrait être inséré à gauche dans la liste triée des nombres premiers
    # 'start' sera l'indice du plus petit nombre premier supérieur ou égal à n
    start = bisect.bisect_left(prime_list, n)
    # Cherche la position où n pourrait être inséré à droite dans la liste triée des nombres premiers
    # 'end' sera l'indice du plus grand nombre premier juste au-dessus de n (si n n'est pas premier, 'end' == 'start')
    end = bisect.bisect_right(prime_list, n)

    if prime_list[start] == n:      # Si le nombre à la position 'start' est exactement égal à n, alors n est premier
        print 0                    # On affiche 0, car la différence de l'intervalle premier entourant n est 0 (n est premier)
    else:
        # Si n n'est pas premier, on affiche la différence entre le premier qui suit n et le premier qui précède n
        # prime_list[end] : le premier nombre premier strictement supérieur à n
        # prime_list[start - 1] : le plus grand nombre premier plus petit que n
        print prime_list[end] - prime_list[start - 1] # Affiche la différence, correspondant à la longueur de l'intervalle entre les deux premiers qui encadrent n