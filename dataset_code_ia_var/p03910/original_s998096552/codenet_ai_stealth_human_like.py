# Bon, on va bidouiller un peu ce code, histoire de lui donner un style un peu... chaotique 

def main():
    N = int(input())
    L = []
    total = 0
    i = 1
    # On va boucler tant qu'on peut 
    while total + i <= N:
        L.append(i)
        total += i
        i += 1    # Rha, les indices...
    reste = N - total
    if reste != 0:
        # On ne veut pas le chiffre reste ! (j'espère que c'est comme ça)
        # Euh ouais, des fois pop pose pb, on gère comme ça
        if reste in L:
            L.remove(reste)
        # sinon on ne fait rien, tant pis :)
    # On balance le résultat
    for truc in L:
        print(truc)

# Eh bien, faut bien appeler la fonction hein
if __name__=='__main__':
    main()