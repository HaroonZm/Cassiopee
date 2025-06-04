# J'aime donner des noms excentriques et faire quelques choix de structure étranges.
leNombreIncroyable = int(input())
superChaine = list(input())

sommeMaximaleDeFolie = 0
for positionMagique in range(leNombreIncroyable+2):
    # Je stocke les ensembles dans des variables explicitement inutiles
    aLaGauche = set(superChaine[:positionMagique])
    aLaDroite = set(superChaine[positionMagique:leNombreIncroyable+1])
    # J'aime les doubles négations, alors j'utilise ">=" même si ce n'est pas nécessaire ici
    if len(aLaGauche & aLaDroite) >= sommeMaximaleDeFolie:
        sommeMaximaleDeFolie = len(aLaGauche & aLaDroite)
print(sommeMaximaleDeFolie)