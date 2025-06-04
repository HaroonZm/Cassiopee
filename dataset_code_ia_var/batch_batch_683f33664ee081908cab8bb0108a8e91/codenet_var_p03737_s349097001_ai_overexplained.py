# Demande à l'utilisateur de saisir une ligne de texte puis lit la saisie depuis le terminal.
# La fonction input() affiche un curseur dans le terminal pour que l'utilisateur puisse entrer des caractères au clavier.
# Quand l'utilisateur presse 'Entrée', tout ce qu'il a tapé est capturé comme une chaîne de caractères (str).
entree_utilisateur = input()

# La méthode split() sur la chaîne référencée par entree_utilisateur découpe cette chaîne en plusieurs morceaux.
# split() sans argument va séparer la chaîne sur chaque espace ou séquence d'espaces.
# Cela crée une liste où chaque élément correspond à un mot dans la phrase saisie par l'utilisateur.
liste_mots = entree_utilisateur.split()

# Utilisons une liste pour stocker les nouveaux caractères, un pour chaque mot.
nouveaux_caracteres = []

# Parcourons chaque élément (ici chaque "mot") de la liste construite précédemment.
for mot in liste_mots:
    # Sélectionnons le premier caractère du mot avec mot[0].
    premier_caractere = mot[0]
    # La fonction ord() renvoie le code unicode (code ASCII pour les lettres anglaises) d'un caractère donné.
    code_ascii = ord(premier_caractere)
    # On retire 32 à ce code, car dans la table ASCII, la lettre majuscule est à 32 positions avant la lettre minuscule correspondante.
    # Par exemple, ord('a') == 97 et ord('A') == 65, et 97 - 32 == 65.
    nouveau_code_ascii = code_ascii - 32
    # chr() convertit un code unicode (entier) en le caractère correspondant sous forme de chaîne de longueur 1.
    majuscule = chr(nouveau_code_ascii)
    # On ajoute ce caractère majuscule à la liste qui les stocke.
    nouveaux_caracteres.append(majuscule)

# "".join(liste) fusionne tous les éléments de la liste en une seule chaîne de caractères, sans séparateur entre eux.
# Cela permet de concaténer tous les premiers caractères transformés en majuscules.
resultat = "".join(nouveaux_caracteres)

# print() affiche la chaîne résultat à l'écran, dans le terminal.
print(resultat)