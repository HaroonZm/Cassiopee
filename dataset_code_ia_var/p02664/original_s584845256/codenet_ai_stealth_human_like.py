# Bon bah on commence par choper l'entrée...
t = list(input())

x = len(t) # je crois qu'il faut la taille ?

# On remplace tous les ? par D - logique nan
for idx in range(x):
    if (t[idx] == '?'):
        t[idx] = 'D' # Remplacer par 'D', autant faire simple

# Affichage, ça pourrait être fait autrement, mais bon...
for lettre in t:
    print(lettre, end='') # J'aurais mis end="" mais c'est pareil je crois ?