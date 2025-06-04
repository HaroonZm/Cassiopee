sx_sy_tx_ty = input().split()
sx = int(sx_sy_tx_ty[0])
sy = int(sx_sy_tx_ty[1])
tx = int(sx_sy_tx_ty[2])
ty = int(sx_sy_tx_ty[3])

d = tx - sx
h = ty - sy

route = ''
route = route + 'U' * h
route = route + 'R' * d
route = route + 'D' * h
route = route + 'L' * (d + 1)
route = route + 'U' * (h + 1)
route = route + 'R' * (d + 1)
route = route + 'D'
route = route + 'R'
route = route + 'D' * (h + 1)
route = route + 'L' * (d + 1)
route = route + 'U'

print(route)