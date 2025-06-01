import re

def main():
    """
    Lit une chaîne de caractères en entrée, recherche toutes les sous-séquences correspondant au
    motif de zéros ou plusieurs 'J', suivis de zéros ou plusieurs 'O', suivis de zéros ou plusieurs 'I',
    puis calcule le nombre maximal de caractères 'O' dans ces sous-séquences qui respectent les conditions:
    le nombre de 'J' est au moins égal au nombre de 'O' et le nombre de 'I' est au moins égal au nombre de 'O'.

    Affiche ensuite ce nombre maximal.
    """
    # Définition du motif regex : un groupe de 0 ou plusieurs 'J', suivi d'un groupe de 0 ou plusieurs 'O',
    # suivi d'un groupe de 0 ou plusieurs 'I'.
    pat = "(J*)(O*)(I*)"
    ans = 0  # Variable pour stocker la réponse maximale

    # Lecture de la chaîne de caractères depuis l'entrée standard
    s = input()

    # Recherche de toutes les occurrences orthogonales au motif dans la chaîne donnée
    # re.findall retourne une liste de tuples avec trois éléments correspondant aux groupes.
    for match in re.findall(pat, s):
        j = len(match[0])  # Nombre de 'J' dans la séquence correspondante
        o = len(match[1])  # Nombre de 'O' dans la séquence correspondante
        i = len(match[2])  # Nombre de 'I' dans la séquence correspondante

        # Vérification des conditions données : j >= o et i >= o
        # Si elle est respectée, on met à jour la réponse avec la valeur maximale possible de o
        if j >= o and i >= o:
            ans = max(ans, o)

    # Affichage de la réponse finale, soit la longueur maximale du segment de 'O' respectant les contraintes
    print(ans)

# Appel de la fonction principale
if __name__ == "__main__":
    main()