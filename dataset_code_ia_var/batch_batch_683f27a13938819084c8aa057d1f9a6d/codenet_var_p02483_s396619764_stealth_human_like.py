# Bon, on prend l'entrée, en espérant que ce soit 3 nombres...
a = raw_input().split()
a = [int(i) for i in a]

# Juste pour être sûr que la liste soit triée (je préfère sorted mais bon)
a.sort()

# Affichage, comme demandé
print "%d %d %d" % (a[0], a[1], a[2])