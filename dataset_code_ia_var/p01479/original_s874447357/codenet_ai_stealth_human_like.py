# Bon alors, je sais pas... on va faire comme ça
input_str = raw_input()
input_str = input_str.replace('egg', '0')
input_str = input_str.replace('chicken', '1')
# p'tit bidouillage pour mettre des espaces où faut
i = len(input_str) - 2
while i >= 0:
    if input_str[i] == input_str[i + 1]:
        input_str = input_str[:i+1] + " " + input_str[i+1:]
    i -= 1
parts = input_str.split()
# ça trie par longueur décroissante, c'est pas mal
parts = sorted(parts, key=lambda s: len(s), reverse=True)
# bon, on regarde la fin
if parts[0][-1] == "0":
    print "egg"
else:
    print "chicken"