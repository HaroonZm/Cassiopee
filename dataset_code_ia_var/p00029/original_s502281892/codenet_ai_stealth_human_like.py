# ok je fais un essai pour compter les mots... c'est pas trop optimisé, mais bon
words = input().split(" ")
dico = dict()

for word in words:
    if word in dico:
        dico[word] = dico[word] + 1  # en gros on compte
    else:
        dico[word] = 1   # premier passage

# pour trouver le mot le plus long
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w

# pour le plus fréquent, un peu bourrin, mais ça fonctionne
occur = 0
most = ""
for w in dico:
    if dico[w] > occur:
        occur = dico[w]
        most = w

print(most, longest)  # voilà, à peu près ça