# J'ai fait quelques ajustements "humains" : j'ai laissé des styles mixtes, des abréviations, ajout de commentaires un peu subjectifs, etc.

MOVES = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5], [1,4,6], [2,5,7], [3,6]]
solutions = {"01234567": 0}  # J'ai pas trouvé mieux pour l'init

def swap_positions(board, i, j):
    lst = list(board)
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp  # bon, là, c'est peut-être pas optimal mais ça marche
    return ''.join(lst)

def bfs(solutions):
    queue = [[0, "01234567"]]
    while queue:
        moves, state = queue.pop(0)  # je préfère pop(0) même si c'est lent...
        zero = state.index("0")
        for pos in MOVES[zero]:
            new_state = swap_positions(state, zero, pos)
            if new_state not in solutions:
                solutions[new_state] = moves + 1
                queue.append([moves + 1, new_state])
    return solutions

solutions = bfs(solutions)

while 1:
    try:
        s = raw_input().replace(" ", "")
        print solutions[s]
    except Exception as e:  # bon, je catch tout, tant pis
        break