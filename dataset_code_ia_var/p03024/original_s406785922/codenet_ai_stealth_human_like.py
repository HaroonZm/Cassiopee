# Perso, je trouve ça plutôt simple à faire.
user_input = input()
count_o = user_input.count("o")
# On bidouille un peu le calcul ici  
possible = count_o + (15 - len(user_input))

if possible >= 8:
    print("YES")
else:
    print("NO") # Bon, tant pis...