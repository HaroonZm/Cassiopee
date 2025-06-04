n = int(input())  # nb total, bon ça va
a_b = input().split()
a = int(a_b[0])
b = int(a_b[1]) # split en deux var... je préfère ça perso

# liste des valeurs
p = list(map(int, input().split()))

p1=0
p2=0
p3=0
for i in range(len(p)):
    if p[i] <= a:
        p1 = p1 + 1
    elif p[i] <= b:
        p2 += 1
    else:
        p3=p3+1  # j'aurais pu utiliser += partout mais bon

# J'affiche le résultat 
print(min([p1, p2, p3]))
# (ptet qu'il faudrait vérifier si la liste p n'est pas vide mais ici tant pis)