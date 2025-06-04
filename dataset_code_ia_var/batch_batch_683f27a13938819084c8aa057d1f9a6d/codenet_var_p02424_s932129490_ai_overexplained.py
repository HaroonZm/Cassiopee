# Demande à l'utilisateur de saisir deux valeurs entières séparées par un espace
# input() lit la ligne saisie par l'utilisateur (sous forme de texte)
# split() divise cette chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur
# map(int, ...) convertit chaque élément de la liste (qui sont des chaînes de caractères) en un entier (int)
# Les deux valeurs (maintenant des entiers) sont affectées à a et b respectivement
a, b = map(int, input().split())

# Opérations logiques sur les bits :
# &  : AND bit-à-bit. Chaque bit est 1 si les deux bits correspondants de a et b sont 1, sinon 0
# |  : OR bit-à-bit. Chaque bit est 1 si au moins un des bits correspondants de a ou b est 1
# ^  : XOR bit-à-bit. Chaque bit est 1 si les bits correspondants de a et b sont différents

# f-string (chaîne formatée) est utilisée pour mettre en forme la chaîne de sortie
# {valeur:032b} : Cela signifie convertir 'valeur' au format binaire avec un remplissage de zéros à gauche pour obtenir toujours 32 caractères
# '\n' est placé entre chaque résultat pour que chaque valeur apparaisse sur une ligne différente

result_and = a & b     # Calcule le ET bit-à-bit entre a et b
result_or  = a | b     # Calcule le OU bit-à-bit entre a et b
result_xor = a ^ b     # Calcule le OU exclusif bit-à-bit entre a et b

# Formate les résultats en chaînes binaires sur 32 chiffres, avec des zéros ajoutés devant si nécessaire
result_and_str = f"{result_and:032b}"   # Formatage de result_and comme une chaîne binaire de 32 bits
result_or_str  = f"{result_or:032b}"    # Formatage de result_or comme une chaîne binaire de 32 bits
result_xor_str = f"{result_xor:032b}"   # Formatage de result_xor comme une chaîne binaire de 32 bits

# Affiche (imprime) les résultats formatés, chacun sur une nouvelle ligne
print(result_and_str + "\n" + result_or_str + "\n" + result_xor_str)