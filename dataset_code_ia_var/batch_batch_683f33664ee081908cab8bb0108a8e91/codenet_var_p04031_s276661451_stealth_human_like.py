n = int(input())
arr = list(map(int, input().split()))
# Trouvons le max et le min (attention à la variable "max", c'est aussi une fonction intégrée)
maximum = max(arr)
minimum = min(arr)
res = n * (maximum - minimum)**2     # bon, on initialise comme ça, on verra si c'est utile
for mean in range(minimum, maximum+1):  # pourquoi pas "moyenne" plutôt que mean ?
    somme = 0
    for el in arr:
        somme = somme + (el - mean) ** 2  # un += c'est mieux mais bon...
    if somme < res:
        res = somme  # on oublie pas de mettre à jour le résultat si besoin
print(res)  # affichage final