from collections import defaultdict

while True:
    W, H = map(int, input().split())
    if W == 0:
        break
    square = []
    players_dict = {}
    reservation = defaultdict(list)
    goal = []
    dir_dict = {"E": 0, "N": 1, "W": 2, "S": 3}
    dir_diff = ((1, 0), (0, -1), (-1, 0), (0, 1))

    for y in range(H):
        row = list(input())
        square.append(row)
        for x, c in enumerate(row):
            if c in "ENWS":
                players_dict[len(players_dict)] = [x, y, dir_dict[c]]
            elif c == "X":
                goal.append((x, y))

    finished = False
    for step in range(1, 121):
        for i, (x, y, d) in players_dict.items():
            moved = False
            for i_dir in range(d-1, d+3):
                dx, dy = dir_diff[i_dir % 4]
                nx, ny = x + dx, y + dy
                if square[ny][nx] in (".", "X"):
                    players_dict[i][2] = i_dir % 4
                    reservation[(nx, ny)].append(((i_dir - 2) % 4, i))
                    moved = True
                    break
            if not moved:
                reservation[(x, y)].append(((d - 2) % 4, i))

        for pos, lst in list(reservation.items()):
            if len(lst) > 1:
                reservation[pos] = [min(lst)]

        for (nx, ny), lst in reservation.items():
            _id = lst[0][1]
            x, y, d = players_dict[_id]
            players_dict[_id][0], players_dict[_id][1] = nx, ny
            square[y][x], square[ny][nx] = ".", "o"

        reservation.clear()

        remove_ids = []
        for i, (x, y, d) in players_dict.items():
            if (x, y) in goal:
                square[y][x] = "."
                remove_ids.append(i)
        for i in remove_ids:
            del players_dict[i]

        if not players_dict:
            print(step)
            finished = True
            break
    if not finished:
        print("NA")