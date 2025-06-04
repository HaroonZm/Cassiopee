caractere_saisi_par_utilisateur = input()

code_ascii_du_caractere_saisi = ord(caractere_saisi_par_utilisateur)

code_ascii_du_caractere_suivant = code_ascii_du_caractere_saisi + 1

caractere_suivant = chr(code_ascii_du_caractere_suivant)

print(caractere_suivant)