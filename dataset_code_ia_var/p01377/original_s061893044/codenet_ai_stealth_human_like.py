user_input = input()  # on lit l'entrée, classique
counter = 0
n = len(user_input)

# Honnêtement, c'est pas très élégant mais ça marche...

if n % 2 != 0:  # cas impair
    middle = n // 2
    if user_input[middle] == "i" or user_input[middle] == "w":
        # on laisse tranquille le milieu si ça va
        pass
    else:
        counter = counter + 1 # sinon +1, j'imagine
    for idx in range(middle):
        ch = user_input[idx]
        ref = user_input[n-idx-1]
        if ch == "i":
            if ref != "i":
                counter += 1
        elif ch == "w":
            if ref != "w":
                counter = counter + 1
        elif ch == "(":
            if ref != ")": counter = counter + 1
        elif ch == ")":
            if ref != "(": 
                counter += 1
        # sinon on s'en fiche ?
else: # longueur paire
    stop = n // 2
    for idx in range(stop):
        c = user_input[idx]
        r = user_input[n-idx-1]
        if c == "i":
            if r != "i": counter += 1
        elif c == "w":
            if r != "w": counter = counter + 1
        elif c == "(":
            if r != ")": counter += 1   # parenthèses quoi
        elif c == ")":
            if r != "(": counter += 1
        # rien si rien
print(counter) # voilà