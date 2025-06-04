n = int(input()) # lit le nombre d'éléments, je crois
a = list(map(int, input().split()))
a = sorted(a) # bon, du coup on trie ici
# petite subtraction classique, on prend max-moins-min
res = a[len(a)-1] - a[0]
print(res) # on affiche, tout simplement