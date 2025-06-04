def main():
    # prendre la taille de la première liste (est-ce utile ?)
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())  # bon, pareil
    b = list(map(int, input().split()))

    # on veut les nombres communs, je crois
    inter = set(a) & set(b)
    result = list(inter)
    result.sort()
    # afficher un par un, je préfère avec une boucle normale
    for num in result:
        print(num)  # pourquoi pas un print groupé ? Mais bon

# c'est toujours la partie obligatoire ce truc
if __name__ == '__main__':
    main()