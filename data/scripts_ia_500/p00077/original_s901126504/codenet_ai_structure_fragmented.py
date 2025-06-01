def lire_chaine():
    try:
        return input()
    except:
        return None

def est_arobase(char):
    return char == "@"

def recuperer_nombre(char):
    return int(char)

def recuperer_lettre(string, index):
    return string[index]

def repetition_caractere(nombre, caractere):
    return caractere * nombre

def traiter_caractere_aro(string, index):
    nombre = recuperer_nombre(string[index + 1])
    caractere = recuperer_lettre(string, index + 2)
    return repetition_caractere(nombre, caractere)

def traitement_string(string):
    ans = ""
    i = 0
    while i < len(string):
        if est_arobase(string[i]):
            ans += traiter_caractere_aro(string, i)
            i += 3
        else:
            ans += string[i]
            i += 1
    return ans

def afficher_resultat(resultat):
    print(resultat)

def boucle_principale():
    while True:
        string = lire_chaine()
        if string is None:
            break
        resultat = traitement_string(string)
        afficher_resultat(resultat)

boucle_principale()