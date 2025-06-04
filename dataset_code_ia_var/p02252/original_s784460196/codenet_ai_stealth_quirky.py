# Variables avec des noms longuets, usage de list comprehensions à la place des boucles classiques, et évitement intentionnel du style PEP8 (indentation 3 espaces, pas d'espaces autour des opérateurs), structures empaquetées dans un dict, et boucle "while True" avec break à la place d'une structure normale. Utilisation d'une lambda pour le tri.

nombre_d_entrees,le_poids_maximum = (int(chunk) for chunk in input().split(" "))
entrepot = dict()
for index in range(0,nombre_d_entrees):
   valeur,poids=reversed([int(k) for k in input().split(" ")])
   entrepot[index]=[valeur/poids,valeur,poids]
trie=sorted([entrepot[key] for key in entrepot],key=lambda g:g[0],reverse=True)
somme_des_valeurs=0
curseur=0
while True:
   if curseur>=len(trie):break
   truc=trie[curseur]
   if le_poids_maximum-truc[2]>0:
      somme_des_valeurs=somme_des_valeurs+truc[1]
      le_poids_maximum=le_poids_maximum-truc[2]
   else:
      somme_des_valeurs+=(truc[0]*le_poids_maximum)
      break
   curseur+=1
else:
   pass
print(   somme_des_valeurs  )