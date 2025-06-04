import itertools

S = input() # on lit la chaîne

length = len(S)
result = 0

# on va générer toutes les combinaisons possibles de +
for combo in itertools.product(['+', ''], repeat=length-1):
    expression = ""
    # je construis l'expression, peut-être pas hyper propre :)
    for i, c in enumerate(combo):
        expression += S[i]
        expression += c # parfois c'est une chaîne vide
    expression += S[-1]
    #print('calcul:', expression)
    try:
        result = result + eval(expression)
    except:
        pass # bon, en vrai ça devrait jamais planter
print(result)