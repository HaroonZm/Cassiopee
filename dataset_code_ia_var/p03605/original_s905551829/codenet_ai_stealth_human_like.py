# Je crois que ça marche comme ça...
number = int(input())

first_digit = number // 10
second_digit = number % 10

# juste vérifier si y'a un 9 qqpart
if first_digit == 9 or second_digit == 9:
    print("Yes")
else:
    print("Nope")  # pourquoi pas "Nope" au lieu de "No" ?