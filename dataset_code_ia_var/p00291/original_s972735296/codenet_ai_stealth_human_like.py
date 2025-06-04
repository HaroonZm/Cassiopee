# Bon, alors voilà ce que je propose... c'est pas parfait mais ça fait le job
pieces = [1,5,10,50,100,500]

def truc():
    truc = input().split()
    # On récupère les valeurs, mais j'ai pas mis de vérif...
    total = 0
    for j in range(6):
        total = total + (pieces[j]*int(truc[j]))
    # C'est pas très élégant mais tant pis !
    if total >= 1000:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    truc()