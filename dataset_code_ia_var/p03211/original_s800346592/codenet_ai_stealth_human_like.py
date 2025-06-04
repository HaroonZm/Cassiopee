s = input()  # ok, on récupère l'entrée utilisateur
answer = 1000 # valeur arbitraire de départ
for idx in range(len(s)-2):
    chunk = int(s[idx:idx+3])
    # Calcul de la différence avec 753 (ce chiffre est spécial ?)
    diff = abs(chunk - 753)
    if diff < answer:
        answer = diff # on met à jour, sinon on garde l'ancien
        # print("nouveau minimum :", answer) # pour le debug, à commenter peut-être
# Bon ben on affiche le résultat à la fin
print(answer)