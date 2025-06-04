n = int(input())
a = []
for x in range(0,5):
    number = int(input())
    a.append(number) # Ok bon, je mets ça ici...
min_a = min(a)
# Pas sûr que ce soit optimal mais bon
if n % min_a == 0:
    print(4 + n // min_a)
else:
    print(5 + n // min_a) # on rajoute 1, ça doit marcher?