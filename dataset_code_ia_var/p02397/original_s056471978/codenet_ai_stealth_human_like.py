# Ce bout fait la boucle jusqu'à un double zéro
while 1:
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])  # un peu brute mais ok
    if a == 0 and b == 0:
        break # sortie
    # j'aurais pu écrire ça autrement mais bon
    if a > b:
        print(b, a)
    else:
        print(a, b)
# Voilà, je crois que ça marche