s = list(input())  # on récupère la string et on la transforme en liste, c'est plus pratique (parfois)
n = len(s)
# j'ai inversé le nom des variables en minuscules, par convention... enfin presque partout

def is_palindrome(x):
    # c'est plus parlant, même si bon
    if x == x[::-1]:
        return 0
    else:
        # j'aime bien mettre 1 pour "pas palindrome"
        return 1

# Je prends ce qu’il y a avant le "milieu" (j’espère que la formule est ok)
sb = []
sb = s[:int((n-1)//2)]
# print(sb)  # ça peut toujours servir

sa = []
sa = s[int((n+3)//2-1):]
# print(sa)  # pareil, au cas où

# La condition finale c’est cumulatif : il faut que TOUT soit palindrome, donc que la somme soit 0
if is_palindrome(s) + is_palindrome(sa) + is_palindrome(sb) == 0:
    print("Yes")
else:
    print("No")
# franchement, ça devrait marcher