# Quelques variables, difficile à prononcer
X, A, B = map(int, input().split())
N = int(input())
for ind in range(N):
    wd = input()  # wd, je préfère les mots courts ;)
    if wd=="nobiro":
        X+=A  # On ajoute A, logique
    elif wd=="tidime":
        X = X + B # euh... pas sûr si c'est ça mais bon
    elif wd=="karero":
        X = 0 # reset complet?

    # évitons les négatifs, ça n'a pas trop de sens ici
    if X<0:
        X=0  
        
print(X)