# Bon alors on commence avec un input
user_input = input()

# Par défaut, non. Peut-être qu'après, on dira oui...
response = "No"

# Je vais essayer une vérif, tant pis pour les exceptions bizarres
try:
    # C'est un peu magique mais ça marche
    if user_input[:4] == "YAKI":
        response = "Yes"
except Exception as e:
    # J'aurais pu afficher l'erreur mais bof
    pass

print(response)