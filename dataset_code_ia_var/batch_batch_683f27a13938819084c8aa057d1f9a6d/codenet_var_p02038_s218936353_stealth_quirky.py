# Cette version utilise des noms de variables étranges, des opérations en ligne, des listes pour le stockage temporaire, 
# et évite les structures classiques en privilégiant la ternarisation ou des reversements d'ordre.

xXx = int(input())
_l0l_ = input().split()
R3S = ["F", "T"]  # Résultat possible à indexer
po = (lambda a, b: 0 if (a=="T" and b=="F") else 1)(_l0l_[0], _l0l_[1])
Z = [po]
crazy = lambda r, p: 0 if (r == 1 and p == "F") else 1
[o := Z.append(crazy(Z[-1], _l0l_[i+2])) for i in range(xXx-2)]
print(R3S[Z[-1]])