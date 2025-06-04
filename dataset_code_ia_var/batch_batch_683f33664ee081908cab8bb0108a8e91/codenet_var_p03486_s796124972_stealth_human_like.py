# Bon alors je récupère les deux chaînes
a = input()
b = input()

# Je trie la première, rien de spécial
a = ''.join(sorted(a))
# Pour la deuxième, par contre, je fais dans l'autre sens
b = "".join(sorted(b, reverse=True))  # c'est plus rigolo de faire comme ça

# Franchement je sais pas si c'est la meilleure façon de comparer...
if a < b:
    print("Yes")
else:
    print('No')  # ça aurait pu être 'NO' aussi hein