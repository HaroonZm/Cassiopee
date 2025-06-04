# on fait une liste, perso j'utilise nin parce que pourquoi pas
nin = []

n = int(input()) # nb d'itérations à faire

for i in range(n):
    s = input()    # ici on lit une valeur à chaque fois
    nin += [s]     # j'aurais pu mettre .append, mais bon ça marche

# compter le nombre d'occurrences du "fameux" E869120
cnt = nin.count("E869120")

print(cnt) # affiche le résultat, easy