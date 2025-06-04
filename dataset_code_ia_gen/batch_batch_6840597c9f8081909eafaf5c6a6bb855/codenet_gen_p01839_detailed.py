# Solution en Python pour vérifier la correspondance entre les "A" et "Un" dans la conversation

# Approche :
# - Chaque "A" représente une demande de réponse "Un".
# - On garde en mémoire le nombre de "A" non encore "répondu" (compteur en attente).
# - Lorsqu'on rencontre "A", on incrémente ce compteur.
# - Lorsqu'on rencontre "Un", il doit y avoir un "A" non encore apparié ; on décrémente donc ce compteur.
# - Si on rencontre un "Un" alors que le compteur est à zéro, cela veut dire que Goto-san a répondu alors qu'il n'avait pas à le faire => on retourne "NO".
# - A la fin, le compteur doit être zéro (tous les "A" ont reçu leur "Un").
# - Les réponses "Un" peuvent arriver avec un retard, donc l'ordre strict "A" puis "Un" n'est pas obligatoire, tant que le nombre de "Un" ne dépasse jamais le nombre de "A" rencontrés jusqu'au moment.
# - Cela correspond à une vérification classique des parenthèses équilibrées, ici avec "A" ouvrant et "Un" fermant.

# Mise en œuvre :

N = int(input().strip())  # Nombre total d'énoncés (A ou Un)

waiting = 0  # Nombre de "A" non appariés (attendant un "Un")
for _ in range(N):
    s = input().strip()
    if s == "A":
        # Un "A" apparait, on a une attente de réponse "Un"
        waiting += 1
    else:  # s == "Un"
        # Un "Un" apparait, il doit y avoir une attente
        if waiting == 0:
            # Réponse sans "A" préalable
            print("NO")
            break
        waiting -= 1
else:
    # Tous les "Un" ont un "A" correspondant
    # On vérifie si toutes les réponses ont été données (attente à zéro)
    if waiting == 0:
        print("YES")
    else:
        # Reste des "A" sans réponse
        print("NO")