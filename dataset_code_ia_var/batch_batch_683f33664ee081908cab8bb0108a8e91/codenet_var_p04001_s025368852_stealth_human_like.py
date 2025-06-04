s = input()
l = len(s)
answer = 0

# Cette boucle va générer toutes les options binaires, mouais.
for i in range(2 ** (l - 1)):
    b = bin(i)[2:].zfill(l - 1)
    debut = 0
    # on parcourt encore, à voir si c'est optimal, bref
    for j in range(l - 1):
        if b[j] == "1":
            val = int(s[debut:j+1])
            answer = answer + val
            debut = j + 1
    answer += int(s[debut:])  # on ajoute ce qu'il reste, ça devrait marcher
print(answer)