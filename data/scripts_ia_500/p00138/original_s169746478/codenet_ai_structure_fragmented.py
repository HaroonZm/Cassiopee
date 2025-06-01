def lire_valeurs():
    n, t = map(float, raw_input().split())
    return n, t

def remplir_dictionnaire():
    d = {}
    for _ in range(8):
        n, t = lire_valeurs()
        d[t] = int(n)
    return d

def trier_cles(d):
    return sorted(d)

def ajouter_premiers_au_O(ls, d, O):
    for j in ls[:2]:
        O.append((d[j], j))

def ajouter_autres_au_dic(ls, d, dic):
    for j in ls[2:]:
        dic[j] = d[j]

def traiter_donnees():
    O = []
    dic = {}
    for _ in range(3):
        d = remplir_dictionnaire()
        ls = trier_cles(d)
        ajouter_premiers_au_O(ls, d, O)
        ajouter_autres_au_dic(ls, d, dic)
    return O, dic

def ajouter_premiers_dic_au_O(dic, O):
    for i in sorted(dic)[:2]:
        O.append((dic[i], i))

def afficher_resultat(O):
    for i in O:
        print i[0], i[1]

def main():
    O, dic = traiter_donnees()
    ajouter_premiers_dic_au_O(dic, O)
    afficher_resultat(O)

main()