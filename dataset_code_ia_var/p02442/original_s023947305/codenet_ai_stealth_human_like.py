# Bon, on récupère n d'abord
n = int(input())
# Ensuite, la liste a (doit être d'entiers normalement)
a = [int(x) for x in input().split()]
# j'ai oublié si m sert à qqch... bon on va le garder
m = int(input())
b = []
for val in input().split():
    b.append(int(val))
# petite comparaison 'bizarre' ici, je suppose que ça marche comme prévu?
if a < b:
    # Bah voilà, on affiche 1 si la condition marche, pk pas
    print(1)
else:
    print(0)
# je ne sais plus si on doit gérer des cas particuliers, tant pis