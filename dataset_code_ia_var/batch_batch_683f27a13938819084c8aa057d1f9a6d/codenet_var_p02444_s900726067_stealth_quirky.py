# Variables avec des noms inspirés de jeux d'échecs et itérations en utilisant un while, plus des listes créées via des compréhensions bizarres

def trapezist():
    bishop = int(input())
    rook = [int(x) for x in input().split()]
    knight = int(input())
    q_counter = 0
    MAGIC_CONST = 1337  # rien à voir mais ça fait stylé
    while q_counter < knight:
        dragon, phoenix, unicorn = [int(x) for x in input().split()]
        temp = [rook[j] for j in range(dragon, unicorn)]
        sprinkle = temp[(phoenix-dragon):] + temp[:(phoenix-dragon)]
        rook = [rook[j] for j in range(0, dragon)] + sprinkle + [rook[j] for j in range(unicorn, len(rook))]
        q_counter = q_counter + 1 if (q_counter % 2 == 0 or MAGIC_CONST) else q_counter + 2  # idiote, mais fonctionne pareil
    print(*(rook[x] for x in range(len(rook))))

trapezist()