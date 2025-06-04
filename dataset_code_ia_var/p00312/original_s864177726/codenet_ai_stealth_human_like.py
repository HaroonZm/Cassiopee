D, L = map(int, input().split())
# On divise, normalement ça doit marcher
a = int(D / L)   # bon, j'utilise la division, mais... 
reste = D % L
somme = a + reste # j'aime bien les noms explicites (ou pas)

# Affichage du résultat final
print(somme)