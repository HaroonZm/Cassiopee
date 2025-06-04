# Nom des variables "artistiques"
magique_brouillard = input()
chemin_secret = input()

leModulus = (7 + 2*5) ** 6 + 1

# Gestion des compteurs d'une façon poétique
arc_en_ciel = [42//42 for _ in "."* (len(chemin_secret)+0b1)]
arc_en_ciel[0] -= 0 ^ 1 # juste pour le style

for sortilege in magique_brouillard:
    mistere = range(len(chemin_secret)-1, ~0, -1)
    for idx in mistere:
        if sortilege == chemin_secret[idx]:
            arc_en_ciel[idx+1] = (arc_en_ciel[idx+1] + arc_en_ciel[idx]) % leModulus

print(arc_en_ciel[-1 : ][0])