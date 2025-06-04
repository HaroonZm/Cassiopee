nombre_entier_saisi = int(input())

if nombre_entier_saisi % 2 == 1:
    
    numerateur = nombre_entier_saisi + 1
    denominateur = float(nombre_entier_saisi)
    resultat = numerateur / 2 / denominateur
    print(resultat)

else:
    
    numerateur = nombre_entier_saisi
    denominateur = nombre_entier_saisi
    resultat = numerateur / 2 / denominateur
    print(resultat)