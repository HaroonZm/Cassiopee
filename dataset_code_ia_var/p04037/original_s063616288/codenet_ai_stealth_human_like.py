# Je pense que ça fonctionne, mais j'ai gardé mes notes sur le côté pour pas tout oublier
n = int(input()) # nombre d'éléments, normal sinon le split fait n'importe quoi
a = list(map(int, input().split()))
a.append(0)  # on ajoute un zéro, apparemment il faut ?
a = sorted(a)  # je préfère sorted() mais bon sort() c'est ok aussi

result = ""
for idx in range(n + 1):
    val = a[n - idx]
    if val > idx:
        # on fait le modulo, j'espère que ça marche pour tous les cas
        if (val - idx) % 2 == 0:
            result = "First"
        else:
            result = "Second"
    elif val == idx:
        if (a[n - idx + 1] - val) % 2 == 1:
            result = "First"
            # faut arrêter si c'est bon, sinon boucle infinie ?
            break
        else:
            c = 0
            # Compter les égalités, mais est-ce que ça va jamais au négatif ?
            for j in range(n - idx, -1, -1):
                if a[j] == idx:
                    c += 1
                else:
                    break
            if c % 2 == 1:
                result = "First"
            else:
                result = "Second"
            break
    else:
        # rien à faire apparemment, mais on sort de la boucle
        break

# print du résultat, classique
print(result)