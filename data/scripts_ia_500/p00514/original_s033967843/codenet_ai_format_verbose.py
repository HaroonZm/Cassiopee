nombre_lignes, nombre_colonnes, valeur_entree = map(int, input().split())

valeur_reste = valeur_entree - nombre_colonnes * nombre_lignes

if valeur_reste < 0:
    
    print(0)
    
else:
    
    facteur_denominateur = 1
    for indice_denominateur in range(valeur_reste):
        facteur_denominateur *= indice_denominateur + 1
    
    facteur_numerateur = 1
    for indice_numerateur in range(valeur_reste):
        facteur_numerateur *= indice_numerateur + nombre_colonnes
    
    resultat = facteur_numerateur // facteur_denominateur
    print(resultat)