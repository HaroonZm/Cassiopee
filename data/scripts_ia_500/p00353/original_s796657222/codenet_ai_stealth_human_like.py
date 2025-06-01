a, b, c = map(int, input("Enter three numbers separated by space: ").split())

# Bon, on regarde si a est déjà plus grand ou égal à c, dans ce cas rien à faire
if a >= c:
    print(0)
else:
    diff = c - a  # calcule la différence
    if diff <= b:
        print(diff)
    else:
        print("NA")  # pas possible dans le délai, je suppose