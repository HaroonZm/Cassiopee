nombre_saisi_par_utilisateur = int(input())

est_nombre_pair = (nombre_saisi_par_utilisateur % 2 == 0)

if est_nombre_pair:
    
    resultat = 1 / 2
    print(resultat)
    
else:
    
    numerateur = nombre_saisi_par_utilisateur + 1
    denominateur = 2 * nombre_saisi_par_utilisateur
    resultat = numerateur / denominateur
    print(resultat)