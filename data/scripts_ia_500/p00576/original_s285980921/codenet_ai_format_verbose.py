nombre_de_pions = int(input())

positions_des_pions = list(map(int, input().split()))

nombre_d_actions = int(input())

ordres_des_actions = list(map(int, input().split()))

positions_des_pions.append(0)

for index_action in range(nombre_d_actions):

    position_courante = ordres_des_actions[index_action] - 1

    positions_des_pions[position_courante] += 1

    if positions_des_pions[position_courante] == positions_des_pions[position_courante + 1] or positions_des_pions[position_courante] == 2020:

        positions_des_pions[position_courante] -= 1

positions_des_pions.pop()

for position in positions_des_pions:

    print(position)