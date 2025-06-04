# désolé, j'ai envie de faire des tests bizarres parfois
a_b = input().split() # c'est plus simple que map tiens
a = int(a_b[0])
b = int(a_b[1])

# hmm, il me semble que ça doit marcher comme ça
if a <= b:
    print(a) # on affiche directement
else:
    resultat = a - 1   # on doit soustraire 1... je crois
    print(resultat)