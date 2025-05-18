cou = 0 
i = input(). lower()
while True:
    j = []
    j = input(). split()
    if j[0] == "END_OF_TEXT": break
    k = [x.lower() for x in j]
    cou += k.count(i)

print(cou)