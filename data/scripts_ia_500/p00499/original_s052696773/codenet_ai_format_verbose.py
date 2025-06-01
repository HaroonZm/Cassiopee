longueur_liste = int(input())
longueur_rectangle = int(input())
largeur_rectangle = int(input())
longueur_decoupe = int(input())
largeur_decoupe = int(input())

if longueur_rectangle % longueur_decoupe == 0 and largeur_rectangle % largeur_decoupe == 0:
    
    nombre_decoupes_longueur = longueur_rectangle // longueur_decoupe
    nombre_decoupes_largeur = largeur_rectangle // largeur_decoupe
    
    nombre_decoupes_longueur, nombre_decoupes_largeur = sorted([nombre_decoupes_longueur, nombre_decoupes_largeur])
    
    print(longueur_liste - nombre_decoupes_largeur)

elif longueur_rectangle % longueur_decoupe == 0 and largeur_rectangle % largeur_decoupe != 0:
    
    nombre_decoupes_longueur = longueur_rectangle // longueur_decoupe
    nombre_decoupes_largeur = (largeur_rectangle // largeur_decoupe) + 1
    
    nombre_decoupes_longueur, nombre_decoupes_largeur = sorted([nombre_decoupes_longueur, nombre_decoupes_largeur])
    
    print(longueur_liste - nombre_decoupes_largeur)

elif longueur_rectangle % longueur_decoupe != 0 and largeur_rectangle % largeur_decoupe == 0:
    
    nombre_decoupes_longueur = (longueur_rectangle // longueur_decoupe) + 1
    nombre_decoupes_largeur = largeur_rectangle // largeur_decoupe
    
else:
    
    nombre_decoupes_longueur = (longueur_rectangle // longueur_decoupe) + 1
    nombre_decoupes_largeur = (largeur_rectangle // largeur_decoupe) + 1
    
    nombre_decoupes_longueur, nombre_decoupes_largeur = sorted([nombre_decoupes_longueur, nombre_decoupes_largeur])
    
    print(int(longueur_liste - nombre_decoupes_largeur))