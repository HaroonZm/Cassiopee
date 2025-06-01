import math
f = 100000
n = int(input())  # nombre de fois qu'on va appliquer l'augmentation
for _ in range(n):
    f = f * 1.05
    # je prends le plafond au millier le plus proche
    f = int(math.ceil(f / 1000) * 1000)
    
print(f)  # affichage final du prix après augmentations