import re

total = 0
while 1:
    try:
        line = input()
        # On cherche les nombres...
        regex = re.compile('\d+')
        found = regex.findall(line)
        # parse (ça pourrait planter si jamais!)
        res = [int(i) for i in found]
        total = total + sum(res)
    except EOFError:
        # Fin des entrées
        break

print(total)
# fin !