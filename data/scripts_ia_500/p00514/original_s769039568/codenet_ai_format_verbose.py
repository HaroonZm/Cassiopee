def calculer_nombre_de_combinaisons():
    
    nombre_lignes, nombre_colonnes, valeur_r = map(int, input().split())
    
    valeur_r_reduite = valeur_r - (nombre_lignes * nombre_colonnes)
    
    if valeur_r_reduite < 0:
        print(0)
    else:
        from math import factorial as factorielle
        
        numerateur = factorielle(nombre_lignes + valeur_r_reduite - 1)
        denominateur = factorielle(valeur_r_reduite) * factorielle(nombre_lignes - 1)
        
        resultat = numerateur // denominateur
        
        print(resultat)
        

if __name__ == "__main__":
    calculer_nombre_de_combinaisons()