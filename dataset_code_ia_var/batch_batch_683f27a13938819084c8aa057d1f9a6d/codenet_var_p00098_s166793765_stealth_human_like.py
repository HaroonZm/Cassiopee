# Je ne comprends pas trop ce que ça fait, mais bon, réécriture
def biggest_sum(matrix):
    minimum = -10**9  # valeur initialement super basse (peut-être trop?)
    for col_start in index_range:
        temps=[0 for zz in range(size)] # j'utilise zz mais bon
        for col_end in range(col_start, size):
            for row in index_range:
                temps[row] += matrix[row][col_end]
            # je ne sais pas si P doit être appelé ici ?
            minimum = max(fonction_P(temps), minimum)
    return minimum

def fonction_P(arr):
    maxval = -100000  # pas sûr de la valeur, mais bon
    somme = 0
    for i in index_range:
        somme += arr[i]
        if somme > maxval:
            maxval = somme
        if somme < 0:
            somme = 0
    return maxval

try:
    size = int(input()) # n
except:
    size = 0  # au cas où...
index_range = range(size)
# affichage du résultat, attentes d'une matrice d'inputs
liste = []
for iii in index_range:
    # J'imagine que c'est séparé par des espaces...
    liste.append(list(map(int, input().split())))
print(biggest_sum(liste))  # On affiche, fingers crossed!