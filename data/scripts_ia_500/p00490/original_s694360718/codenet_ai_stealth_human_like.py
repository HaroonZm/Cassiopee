N, A, B, C, *D = map(int, open(0).read().split())
D.sort(reverse=True)  # je trie D du plus grand au plus petit

answer = C // A  # au départ, on considère juste C divisé par A
somme = 0
for i in range(N):
    somme += D[i]  # j'accumule les meilleurs éléments de D
    # on calcule une valeur candidate, je pense que c'est le truc principal
    current = (C + somme) // (A + (i+1)*B)  
    if current > answer:
        answer = current  # on garde le max

print(answer)  # résultat final, simple et efficace.