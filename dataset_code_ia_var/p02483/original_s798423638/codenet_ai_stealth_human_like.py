# Bon, on récupère les valeurs ici :
user_input = raw_input()
arr = user_input.split(" ")  # je préfère mettre un espace mais bon...

# trie la liste, on va garder ça comme ça...
arr.sort()

for n in arr:
    print n, # affichage sur la même ligne, attention y'a un espace à la fin
# Voilà, c'est à peu près ça !