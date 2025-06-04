# On va demander un entier à l'utilisateur, tout simplement.
n = int(input())
ans = 0

if n == 0:
    ans = 0  # Bon on fait rien si c'est zéro
elif n % 2 != 0:  # Je crois bien que si c'est impair y a un souci
    ans = 0
else:
    power = 10
    while power <= n:
        ans = ans + (n // power) # On monte la puissance à chaque fois (par 5 ou plutôt par 10 ?)
        # power *= 10  # attendez non, c'était 5 dans l'autre code...
        power = power * 5

print(ans)  # voilà le résultat, normalement