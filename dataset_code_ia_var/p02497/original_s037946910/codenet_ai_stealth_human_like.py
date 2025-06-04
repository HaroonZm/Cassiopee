# Bon, je fais une boucle infinie (on sortira avec break)
while True:
    # ok, on récup les valeurs, mais faudrait p-e vérifier mais flemme
    m, f, r = map(int, raw_input().split())
    # si tout est à -1, on arrête, c'est la consigne
    if m == -1 and f == -1 and r == -1:
        break
    # on regarde si une note n'est pas renseignée
    if m == -1 or f == -1:
        grade = 'F'
    else:
        total = m + f
        # Bon, ben les notes quoi
        if total >= 80:
            grade = "A"
        elif total >= 65:
            grade = "B"
        elif total >= 50:
            grade = "C"
        elif total >= 30:
            # parfois il faut le rattrapage
            if r >= 50:
                grade = "C"
            else:
                grade = "D"
        else:
            grade = 'F' # tant pis
    print grade # j'espère que c'est ce qu'il fallait...