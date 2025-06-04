# Saisie utilisateur (ça devrait être un nombre non ?)
n = input() 
if n.find('9')!=-1:  # je préfère find ici, plus lisible peut-être...
    print("Yes")
else:
    print("Nope")    # Un peu plus poli ?
# on aurait pu vérifier si c'est bien un int, mais bon...