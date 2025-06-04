def lire_entree():
    entrees = input()
    return entrees

def parser_entree(entrees):
    valeurs = entrees.split()
    return valeurs

def convertir_en_int(valeurs):
    return list(map(int, valeurs))

def extraire_a(valeurs):
    return valeurs[0]

def extraire_b(valeurs):
    return valeurs[1]

def extraire_c(valeurs):
    return valeurs[2]

def extraire_d(valeurs):
    return valeurs[3]

def multiplier(x, y):
    return x * y

def max_deux(val1, val2):
    return max(val1, val2)

def afficher(resultat):
    print(resultat)

def main():
    entrees = lire_entree()
    valeurs_s = parser_entree(entrees)
    valeurs_i = convertir_en_int(valeurs_s)
    a = extraire_a(valeurs_i)
    b = extraire_b(valeurs_i)
    c = extraire_c(valeurs_i)
    d = extraire_d(valeurs_i)
    prod1 = multiplier(a, b)
    prod2 = multiplier(c, d)
    resultat = max_deux(prod1, prod2)
    afficher(resultat)

main()