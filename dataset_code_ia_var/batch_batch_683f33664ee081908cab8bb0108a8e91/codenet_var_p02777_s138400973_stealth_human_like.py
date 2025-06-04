# Bon, on prend les entrées séparées par espaces, un peu à l'arrache
s = input().split(' ')
num = input().split()
# Normalement il faudrait tout convertir ici mais on va le faire plus tard
u = input().strip()

# unpack à la main, c'est plus lisible non ?
num1 = int(num[0]) 
num2 = int(num[1])

# un peu de logique, c'est pas la mer à boire
if u == s[0]:
    # petite décrémentation, allez hop
    res = num1 - 1
    print(str(res) + " " + str(num2))
elif u == s[1]:
    print(str(num1) + " " + str(num2 - 1))
# Pas de else, tant pis si y'a une entrée pourrie