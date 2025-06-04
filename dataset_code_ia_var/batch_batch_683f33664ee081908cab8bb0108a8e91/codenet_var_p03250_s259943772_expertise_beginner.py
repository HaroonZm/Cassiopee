if __name__ == '__main__':
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])

    # Met les nombres dans une liste
    liste = [a, b, c]
    # Trie la liste du plus grand au plus petit
    liste.sort()
    liste.reverse()

    # Calcule le résultat
    resultat = liste[0] * 10 + liste[1] + liste[2]

    print(str(resultat))