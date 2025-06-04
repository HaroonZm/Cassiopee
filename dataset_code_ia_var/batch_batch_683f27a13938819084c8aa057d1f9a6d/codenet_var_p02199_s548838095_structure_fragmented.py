def lire_entiers_ligne():
    return list(map(int, input().split()))

def extraire_a_valeurs(t):
    return t[0], t[1]

def extraire_pqr_valeurs(t):
    return t[0], t[1], t[2]

def obtenir_a():
    return lire_entiers_ligne()

def obtenir_pqr():
    return lire_entiers_ligne()

def calculer_diff(a, b):
    return b - a

def calculer_pb(p, b):
    return p * b

def calculer_bmoinsaq(b, a, q):
    return calculer_diff(a, b) * q

def calculer_pqur(p, b, a, q):
    return calculer_pb(p, b) - calculer_bmoinsaq(b, a, q)

def calculer_quotient(valeur, denominateur):
    return valeur / denominateur

def calculer_qr(q, r):
    return q + r

def somme_b_result(b, result):
    return b + result

def main():
    ligne1 = obtenir_a()
    a, b = extraire_a_valeurs(ligne1)
    ligne2 = obtenir_pqr()
    p, q, r = extraire_pqr_valeurs(ligne2)
    diff_pb_maq = calculer_pqur(p, b, a, q)
    denom = calculer_qr(q, r)
    quotient = calculer_quotient(diff_pb_maq, denom)
    resultat_final = somme_b_result(b, quotient)
    print(resultat_final)

main()