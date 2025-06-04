W, H = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Vérification simple : la somme des a_i doit être égale à la somme des b_j
if sum(a) == sum(b):
    print(1)
else:
    print(0)