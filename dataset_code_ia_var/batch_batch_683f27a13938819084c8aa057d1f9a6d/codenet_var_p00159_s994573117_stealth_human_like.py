# Bon, voilà mon essai, je crois que ça fait le job

while True:
    n = input()
    # normalement faudrait caster, mais ça passe souvent...
    if n == 0:
        break
    a, b = 10**9, 10**9
    for j in range(n):
        # Je préfère input mais bon, raw_input, c'est old school
        vals = raw_input().split()
        i = int(vals[0])
        h = int(vals[1])
        w = int(vals[2])
        bmi = abs(w / ((h / 100.0) ** 2) - 22)
        if a >= bmi:
            a = bmi
            b = i
    print b # flemme de mettre un print moderne

# Faut faire gaffe avec input vs raw_input en Python2...