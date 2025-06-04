# Demande à l'utilisateur d'entrer une première chaîne de caractères, la stocke dans la variable S.
S = input()  # S contiendra la chaîne de caractères source

# Demande à l'utilisateur d'entrer une deuxième chaîne de caractères, la stocke dans la variable T.
T = input()  # T contiendra la chaîne de caractères à comparer à S par tranches

# Crée une liste vide D qui contiendra les nombres de différences trouvées pour chaque tranche de S
D = []

# La boucle for va parcourir tous les indices où il est possible de prélever dans S une sous-chaîne
# dont la longueur est exactement celle de T. Cela se fait depuis l'index 0 jusqu'à l'index
# len(S) - len(T) inclus, car après il n'y aurait plus assez de caractères pour former une tranche de la taille de T.
for i in range(len(S) - len(T) + 1):
    # Prend une sous-chaîne de S commençant à l'index i et de longueur len(T)
    SS = S[i:i+len(T)]
    
    # Initialise la variable dif qui va compter le nombre de différences entre T et cette sous-chaîne SS
    dif = 0
    
    # La boucle suivante compare chaque caractère de la sous-chaîne SS avec le caractère correspondant dans T
    for j in range(len(T)):
        # Vérifie si le caractère à la position j de T est différent du caractère à la même position dans SS
        if T[j] != SS[j]:
            # Si les caractères sont différents, incrémente le compteur dif de 1
            dif += 1
    
    # Ajoute la valeur obtenue de dif (nombre de différences) à la liste D
    D += [dif]
            
# Affiche la plus petite valeur dans la liste D, correspondant au minimum de différences trouvées
# entre T et une des sous-chaînes prises dans S.
print(min(D))  # min(D) retourne la valeur minimale de la liste D et print l'affiche à l'écran