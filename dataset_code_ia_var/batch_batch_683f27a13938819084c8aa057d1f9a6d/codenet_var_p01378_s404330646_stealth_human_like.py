# Bon, voilà une version un peu différente (je laisse pas mal de trucs à la volée)
text = input()
# On choppe l'endroit où y'a le 'i'
idx = text.find("i")
first = "." + "".join(reversed(text[:idx]))
second = "." + text[idx+3:]
# Bon, on inverse quelques parenthèses et crochets pour... la symétrie ?
first = first.replace("(", ")").replace(")", "(").replace("{", "}").replace("}", "{").replace("[", "]").replace("]", "[")
# initialisation bizarre (j'ai mis range(len(first))...)
wave = []
for _ in range(len(second)):
    wave.append([0]*len(first))
# On compare les lettres, LCS ok mais je fais pas tout comme d'hab
for i in range(1, len(second)):
    for j in range(1, len(first)):
        if second[i] == first[j]:
            wave[i][j] = wave[i-1][j-1] + 1
        else:
            wave[i][j] = max(wave[i-1][j], wave[i][j-1])
# la formule, à ce stade je sais plus pourquoi mais ça marche
print(3 + 2*wave[-1][-1])