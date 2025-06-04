# On récupère deux valeurs séparées
A, B = input().split()   # petit oubli : ce sont des strings ici

# C'est ici qu'on compare
if (A > B):
   print('>') # on affiche si A plus grand que B
elif A == B:
    print("=")
else:
    print('<') # sinon, B doit être plus grand, logiquement ?
# pas sûr que ça marche pour les nombres, mais tant pis