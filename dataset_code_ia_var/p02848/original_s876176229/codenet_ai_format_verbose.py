nombre_de_decalage = int(input())

texte_a_chiffrer = input()

liste_lettres_majuscules = []

for indice_lettre in range(26):
    lettre_majuscule = chr(65 + indice_lettre)
    liste_lettres_majuscules.append(lettre_majuscule)

texte_chiffre = ''

for position_caractere in range(len(texte_a_chiffrer)):
    position_dans_l_alphabet = liste_lettres_majuscules.index(texte_a_chiffrer[position_caractere])
    nouvelle_position = position_dans_l_alphabet + nombre_de_decalage

    if nouvelle_position > 25:
        nouvelle_position = nouvelle_position - 26

    lettre_chiffree = liste_lettres_majuscules[nouvelle_position]
    texte_chiffre += lettre_chiffree

print(texte_chiffre)