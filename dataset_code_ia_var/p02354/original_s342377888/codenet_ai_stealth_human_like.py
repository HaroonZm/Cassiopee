# Bon, on va y aller à la main pour ce script, j'ai mis une grosse valeur à l'arrache pour l'infini
INFINITY = 10**18

n, s_required = map(int, input().split())
listeA = list(map(int, input().split()))

answer = INFINITY

right = 0
current_sum = 0

for left in range(n):
    # On étend right pour dépasser ou atteindre S, logique de fenetre glissante
    while right < n and current_sum < s_required:
        current_sum += listeA[right]
        right += 1
    if current_sum >= s_required:
        temp_res = right - left
        if temp_res < answer:
            answer = temp_res  # on garde la plus petite taille trouvée
    current_sum -= listeA[left]  # on vire l'élément de gauche (un oubli ici serait fatal...)

# En vrai, si jamais answer n'a pas changé, on renvoie 0 parce que c'est pas possible
if answer != INFINITY:
    print(answer)
else:
    print(0)  # sinon, on n'a rien trouvé