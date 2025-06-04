# Définition d'une constante entière qui représente la limite supérieure utilisée pour vérifier la primalité des nombres
MAX = 1000001  # Nous allons vérifier tous les nombres premiers jusqu'à 1 000 000 inclus

# Création d'une liste de booléens, initialement remplie avec la valeur True. Cette liste indiquera si l'indice correspondant est premier (True) ou non (False)
isPrime = [True] * MAX  # Par exemple, isPrime[5] sera True si 5 est premier, sinon False

# Les nombres 0 et 1 ne sont pas des nombres premiers, donc nous les marquons explicitement comme False
isPrime[0] = False
isPrime[1] = False

# Boucle pour appliquer le crible d'Ératosthène : cette méthode permet de trouver tous les nombres premiers jusqu'à MAX - 1 efficacement
# Nous commençons à 2 car 2 est le plus petit nombre premier
# Nous arrêtons à 1000 car (1000 ** 2) = 1 000 000, ce qui couvre tous les nombres dans l'intervalle souhaité
for i in range(2, 1000):
    # Nous vérifions si le nombre i est toujours marqué comme premier
    if isPrime[i]:
        # Si i est premier, alors nous allons marquer tous ses multiples comme non premiers
        # Nous commençons à i**2 car tous les plus petits multiples ont déjà été traités par de plus petits facteurs
        # Nous incrémentons de i à chaque itération, afin de couvrir tous les multiples de i
        for j in range(i ** 2, MAX, i):
            # Nous marquons j comme non premier
            isPrime[j] = False

# Définition d'une fonction qui, étant donnés trois paramètres (a, d, n), trouve le n-ième nombre premier dans une suite arithmétique débutant à a avec un pas d
def solve(a, d, n):
    # Vérifier si le premier terme (a) est un nombre premier
    if isPrime[a]:
        # Si oui, cela compte pour un des n premiers recherchés, donc on décrémente n
        n -= 1
    # Boucle tant qu'il nous reste des nombres premiers à trouver dans la suite
    while n:
        # Incrémenter a de d (passage au prochain élément de la suite arithmétique)
        a += d
        # Vérifier si le nouveau terme est premier
        if isPrime[a]:
            # Si oui, on a trouvé un autre nombre premier, donc on décrémente n
            n -= 1
    # Quand n atteint 0, cela veut dire que le dernier a évalué est le n-ième nombre premier dans la suite arithmétique
    return a

# Définition de la fonction principale qui gère les entrées/sorties et les appels à la fonction solve
def main():
    # Boucle infinie pour traiter une quantité inconnue d'ensembles de données
    while True:
        # Lecture d'une ligne de l'entrée standard, découpée en trois entiers : a, d, n
        # map applique la conversion int sur chaque élément, split découpe l'entrée en morceaux
        a, d, n = map(int, input().split())
        # Test d'arrêt : si a vaut 0, on sort de la boucle
        if a == 0:
            break
        # Appel de la fonction solve avec les paramètres lus et affichage du résultat
        print(solve(a, d, n))

# Appel final pour démarrer le programme principal
main()