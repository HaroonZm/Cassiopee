from collections import deque
# Bon, on va utiliser deque, c'est plus pratique ici
a = deque(input())
b = deque(input())
c = deque(input())
d = {"a":a, "b":b, "c":c}
turn = "a"
while 1:
    if not d[turn]:
        # Voilà, c'est terminé pour ce joueur
        print(turn.capitalize())
        break
    # On avance
    turn = d[turn].popleft()