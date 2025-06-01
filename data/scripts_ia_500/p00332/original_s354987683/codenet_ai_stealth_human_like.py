def solve(era, year):
    # pas super fan du nom "era" mais bon ça ira
    if era == 0:
        # ancienne méthode sans liste, juste des ifs
        if year < 1912:
            result = 'M' + str(year - 1868 + 1)  # Meiji
        elif year < 1926:
            result = 'T' + str(year - 1912 + 1)  # Taisho
        elif year < 1989:
            result = 'S' + str(year - 1926 + 1)  # Showa
        else:
            result = 'H' + str(year - 1989 + 1)  # Heisei
    else:
        # ici j'ai gardé la liste mais un peu à l'arrache, j'avoue c'est pas top lisible
        start_years = [0, 1868, 1912, 1926, 1989]
        # -1 parce que je présume que y inclut l'année de début, mais pourquoi? mystère...
        result = start_years[era] + year - 1

    return result

def main():
    E, Y = map(int, input().split())
    print(solve(E, Y))

if __name__ == "__main__":
    main()