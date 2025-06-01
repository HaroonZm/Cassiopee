N = int(input())
shop_name = input()
boards = [input() for _ in range(N)]

count = 0

for board in boards:
    length_board = len(board)
    length_shop = len(shop_name)
    can_make = False
    for d in range(1, length_board):
        for start in range(length_board):
            # On vérifie si on peut prendre les lettres en partant de start, avec un pas d,
            # pour former le shop_name
            if start + d * (length_shop -1) >= length_board:
                break
            ok = True
            for i in range(length_shop):
                if board[start + i * d] != shop_name[i]:
                    ok = False
                    break
            if ok:
                can_make = True
                break
        if can_make:
            break
    if can_make:
        count += 1

print(count)