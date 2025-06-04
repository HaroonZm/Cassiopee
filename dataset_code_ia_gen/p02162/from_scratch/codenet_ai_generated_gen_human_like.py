T1, T2, R1, R2 = map(int, input().split())

if R1 == -1 or R2 == -1:
    # au moins un des deux n'a pas de rate, on compare les temps
    if T1 < T2:
        print("Alice")
    elif T1 > T2:
        print("Bob")
    else:
        print("Draw")
else:
    # les deux ont un rate
    if R1 > R2:
        print("Alice")
    elif R1 < R2:
        print("Bob")
    else:
        # mêmes rates => égalité, le temps n'est pas pris en compte
        print("Draw")