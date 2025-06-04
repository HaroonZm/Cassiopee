num = int(input())
for nnn in range(num):
    built_train = ""
    s = input()
    j = 0
    # traite par "wagon" de 3 caractères (enfin, normalement)
    while j < len(s):
        if j == 0:
            # premier wagon
            built_train += s[j]
        # Bon, on vérifie la séquence à gauche
        if s[j-2:j] == '->' and built_train[-1] == s[j-3]:
            built_train += s[j]
        # et à droite
        if s[j-2:j] == '<-' and built_train[0] == s[j-3]:
            built_train = s[j] + built_train
        j += 3  # ça saute de 3, un peu dangereux si la saisie est tordue
    print(built_train)