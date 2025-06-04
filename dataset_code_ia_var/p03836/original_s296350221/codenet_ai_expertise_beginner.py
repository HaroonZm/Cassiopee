# Demander les positions de départ et d'arrivée
sx, sy, tx, ty = input().split()
sx = int(sx)
sy = int(sy)
tx = int(tx)
ty = int(ty)

# Calculer la différence horizontale et verticale
lr = tx - sx
ud = ty - sy

# Construire le chemin pas à pas
route = ""
route += "R" * lr
route += "U" * ud
route += "L" * lr
route += "D" * ud
route += "D"
route += "R" * (lr + 1)
route += "U" * (ud + 1)
route += "L"
route += "U"
route += "L" * (lr + 1)
route += "D" * (ud + 1)
route += "R"

print(route)