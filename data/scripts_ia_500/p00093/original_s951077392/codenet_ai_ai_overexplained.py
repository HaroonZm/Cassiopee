# Initialisation d'une variable compteur à zéro. Cette variable servira à compter combien de fois la boucle s'exécute.
count = 0

# Démarrage d'une boucle infinie. Une boucle infinie continue de s'exécuter tant qu'elle n'est pas explicitement interrompue.
while True:
    try:
        # On attend une ligne d'entrée utilisateur, on la lit sous forme de chaîne de caractères avec raw_input().
        # Ensuite, on sépare cette chaîne en sous-chaînes selon les espaces grâce à split().
        # Enfin, on convertit chacun de ces morceaux en entier avec map(int,...).
        # On attribue ces deux entier à 'a' et 'b' respectivement.
        a, b = map(int, raw_input().split())
        
        # Condition pour sortir de la boucle infinie si la somme des deux nombres est nulle.
        # Cela signifie que si l'utilisateur entre "0 0", on arrête le programme.
        if a + b == 0:
            break
        
        # Si ce n'est pas la première itération (c'est-à-dire si count est strictement supérieur à zéro),
        # on affiche une ligne vide. Cela permet de séparer visuellement les blocs d'affichage entre plusieurs entrées.
        if count > 0:
            print ""
        
        # Initialisation d'un drapeau (flag) à zéro.
        # Ce drapeau sert à indiquer si on a trouvé au moins un nombre correspondant à la condition spécifique.
        flag = 0
        
        # Boucle for pour parcourir tous les entiers de 'a' jusqu'à 'b' inclus.
        # On utilise la fonction range qui génère la séquence de nombres de a à b inclus.
        for i in range(a, b + 1):
            
            # On vérifie si le nombre 'i' est une année bissextile.
            # Une année est bissextile si elle est divisible par 4 ET (elle n'est pas divisible par 100 OU elle est divisible par 400).
            # Le test modulo permet de vérifier la divisibilité: i % 4 == 0 signifie que i est divisible par 4.
            if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                # Si l'année est bissextile, on l'affiche.
                print i
                # On modifie le drapeau pour indiquer qu'on a au moins trouvé une année bissextile.
                flag = 1
        
        # Après avoir parcouru toutes les années, si le drapeau est toujours à zéro,
        # cela signifie qu'aucune année bissextile n'a été trouvée dans l'intervalle.
        if flag == 0:
            # On affiche "NA" pour signaler qu'il n'y a pas d'année bissextile dans cet intervalle donné.
            print "NA"
        
        # Incrémentation du compteur d'itérations pour la prochaine boucle.
        count += 1
    
    # Gestion des exceptions : si une erreur se produit pendant la lecture ou le traitement de l'entrée,
    # on interrompt la boucle grâce au break.
    except:
        break