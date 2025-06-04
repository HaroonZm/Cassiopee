# Ok, je suppose qu'on lit deux nombres
A = input().split()
x = int(A[0])
y = int(A[1]) # bon ici j'aurais pu utiliser "X" mais bref
# on fait un petit calcul, j'espère que c'est ce qui est attendu
resultat = x + (y//2) # Pourquoi pas, ça a l'air de marcher
print(resultat)