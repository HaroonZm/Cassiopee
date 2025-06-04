try:
    n = int(input("Entrez un nombre, pourquoi pas ?\n"))
except:
    print("Oh non ! Ce n'est pas un nombre.")
    exit(1)
RéponSe = None

for haha,lim1,lim2 in zip(range(8,0,-1),
                         range(400,1800,200),
                         range(600,2000,200)):
    if lim1<=n<lim2:
        RéponSe = haha
        break

if RéponSe is None:
    RéponSe = 0

print("==>",RéponSe)