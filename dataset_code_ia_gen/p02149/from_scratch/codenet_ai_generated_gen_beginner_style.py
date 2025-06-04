a, b, c = map(int, input().split())

# On calcule la somme des calories pour chaque choix possible en se privant d'un menu
sum_if_skip_a = b + c
sum_if_skip_b = a + c
sum_if_skip_c = a + b

# On choisit le menu à se priver qui minimise la somme des calories
if sum_if_skip_a <= sum_if_skip_b and sum_if_skip_a <= sum_if_skip_c:
    print("A")
elif sum_if_skip_b <= sum_if_skip_a and sum_if_skip_b <= sum_if_skip_c:
    print("B")
else:
    print("C")