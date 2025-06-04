# Bon, donc on lit une chaîne (je sais pas à quoi ça sert)
c = raw_input()  

# là on lit les nombres (ça devrait marcher)
num = raw_input().split()
num = [int(x) for x in num]

num.sort()  # on trie, c'est mieux quand c'est trié

# Je fais une chaîne mais y'a sûrement mieux à faire
s = ""
for i in num:
    s = s + " " + str(i)
print s[1:]  # j’enlève juste le 1er espace comme ça, ça fera joli

# Voilà, c'est pas le code le plus propre mais ça fait le taf je crois