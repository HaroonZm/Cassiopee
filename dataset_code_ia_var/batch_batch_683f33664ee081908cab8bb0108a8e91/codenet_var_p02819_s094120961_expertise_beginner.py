def racine_carree(nombre):
    return nombre ** 0.5

def est_premier(nombre):
    if nombre == 1:
        return False

    i = 2
    while i <= int(racine_carree(nombre)):
        if nombre % i == 0:
            return False
        i += 1

    return True

X = int(input())

if est_premier(X):
    print(X)
    exit()
if X % 2 == 0:
    X = X + 1
while True:
    if est_premier(X):
        print(X)
        break
    X = X + 2