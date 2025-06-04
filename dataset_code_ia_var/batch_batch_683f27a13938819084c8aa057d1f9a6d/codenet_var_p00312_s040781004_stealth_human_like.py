# je fais une liste avec les entiers donnés par l'utilisateur
inputs = list(map(int, input().split()))
# je pense qu'il faut comparer les deux premiers
if inputs[0] < inputs[1]:
    print(inputs[0])  # affiche le plus petit
else:
    # je voulais une sorte de somme bizarre ici...
    res = int(inputs[0] / inputs[1]) + int(inputs[0] % inputs[1])
    print(res)
# fait espérer que ça marche pour tout cas...