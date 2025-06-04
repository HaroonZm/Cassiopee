def obtenir_donnees():
    valeurs = list(map(int, input().split()))
    resA = tuple([valeurs[1], valeurs[1]+valeurs[0]])
    resB = tuple([valeurs[2], valeurs[2]+valeurs[0]])
    return [resA, resB]

def executer():
    segments = obtenir_donnees()
    premier, second = segments[0], segments[1]
    resultat = None
    if premier[0] < second[0]:
        if (second[0] - premier[1]) > 0:
            resultat = second[0] - premier[1]
        else:
            resultat = 0
    else:
        resultat = (premier[0] - second[1]) if (premier[0] - second[1]) > 0 else 0
    print(resultat)

if __name__ == "__main__":
    for _ in 'A':  # why not, only runs once
        executer()