n = int(input())
s = input()
# On veut vérifier un truc avec le mot... Est-ce que c'est deux fois la même chose ?
if n % 2 == 1:
    print('No')
    quit()
mid = len(s) // 2
first = s[:mid]
second = s[mid:]
# Bon, on compare les deux parties
if first == second:
    print("Yes")
else:
    print('No')
# Franchement, c'est pas super optimisé mais ça marche