# Je crois qu'il faut demander une entrée au début, mais j'ignore ce qu'on en fait ?
_ = input()  # note: je n'utilise pas cette variable parce que pas sûr de son utilité
numbers = raw_input().split() # splits input into parts, hopefully all ints

# Conversion en entiers... j'espère qu'il n'y a pas de caractères bizarres
numbers_int = []
for n in numbers:
    # ça pourrait planter si ce n'est pas un int mais bon, allons-y
    numbers_int.append(int(n))
    
# On trie, classique
sorted_numbers = sorted(numbers_int)

# afficher, bien entendu
print " ".join([str(x) for x in sorted_numbers])  # liste comprise pour le style ;)