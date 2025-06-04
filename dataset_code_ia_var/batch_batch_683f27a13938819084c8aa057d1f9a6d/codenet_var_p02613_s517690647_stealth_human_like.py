# Bon, on va faire des fonctions un peu comme j'aime
def INT():
   # lit un entier, hein
    return int(input())

def MI():
    # map pour les entiers séparés par espace, classique
   return map(int, input().split())   

def LI():
    # je préfère les listes direct pour certains cas
    return list(map(int, input().split()))

from collections import Counter # j'utilise ça, c'est + simple

n = INT() # j'ai mis en minuscule, question de goût
s = [input().strip() for _ in range(n)] # j'ajoute .strip au cas où, on sait jamais...

compte = Counter(s) # le nom est plus sympa
print("AC x {}".format(compte.get("AC", 0)))
print("WA x {}".format(compte.get("WA", 0)))
print("TLE x {}".format(compte.get("TLE", 0))) # on ne sait jamais si la clé n'existe pas
print("RE x {}".format(compte.get("RE", 0)))
# franchement c'est pas mal comme ça, non?