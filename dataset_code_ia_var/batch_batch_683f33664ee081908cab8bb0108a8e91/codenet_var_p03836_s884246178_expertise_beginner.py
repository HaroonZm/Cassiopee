sx_sy_tx_ty = input().split()
sx = int(sx_sy_tx_ty[0])
sy = int(sx_sy_tx_ty[1])
tx = int(sx_sy_tx_ty[2])
ty = int(sx_sy_tx_ty[3])

path = ""
for i in range(tx - sx):
    path += "R"
for i in range(ty - sy):
    path += "U"
for i in range(tx - sx):
    path += "L"
for i in range(ty - sy + 1):
    path += "D"
for i in range(tx - sx + 1):
    path += "R"
for i in range(ty - sy + 1):
    path += "U"
path += "L"
path += "U"
for i in range(tx - sx + 1):
    path += "L"
for i in range(ty - sy + 1):
    path += "D"
path += "R"
print(path)