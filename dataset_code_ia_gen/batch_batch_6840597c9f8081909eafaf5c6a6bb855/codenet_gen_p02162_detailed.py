# Lecture des entrées : temps de course et ratings AOJ pour Alice et Bob
T1, T2, R1, R2 = map(int, input().split())

# Cas 1 : Si les deux ont des ratings valides (non -1)
if R1 != -1 and R2 != -1:
    # Si les ratings sont différents, celui avec le rating plus élevé gagne
    if R1 > R2:
        print("Alice")
    elif R1 < R2:
        print("Bob")
    else:
        # Si les ratings sont égaux, c'est un match nul, on regarde pas le temps
        print("Draw")
else:
    # Cas 2 : Au moins un des joueurs n'a pas de rating
    # Dans ce cas, on décide selon le temps : plus court gagne
    if T1 < T2:
        print("Alice")
    elif T1 > T2:
        print("Bob")
    else:
        # Si temps égaux aussi, c'est un match nul
        print("Draw")