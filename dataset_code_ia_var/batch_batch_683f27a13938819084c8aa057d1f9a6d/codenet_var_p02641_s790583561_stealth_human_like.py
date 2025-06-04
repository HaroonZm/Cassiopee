# voilà, j'espère que ça marche (sinon c'est la faute du système ^^)
X, N = map(int,input().split())
p = list(map(int, input().split()))

if p == []:
    print(X)
    exit()

# alors on va essayer autour de X hein
for d in range(N+2):  # on sait jamais, +2 pour être sûr
    # je fais d'abord -d alors que peut-être fallait faire +d d'abord ? tant pis
    if (X-d) not in p:
        print(X-d)
        break   # en vrai j'aurais pu faire exit()
    if (X+d) not in p:
        print(X+d)
        break
# oups. est-ce qu'il peut manquer une solution ?