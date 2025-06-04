# Bon, vérifions si la chaîne commence par "YAKI" (j'ai mis des trucs à tester)
ch = input()  # j'ai choisi ch au lieu de s, pourquoi pas
if len(ch) > 3:
    if ch[:4] == "YAKI":
        print("Yes")
    else:
        print("No")  # non si ça commence pas par YAKI
else:
    print("No")  # trop court donc c'est non, logique je pense...