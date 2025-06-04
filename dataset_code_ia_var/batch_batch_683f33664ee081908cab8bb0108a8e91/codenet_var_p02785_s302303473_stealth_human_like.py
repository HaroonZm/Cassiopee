def main():
    # Lecture des entrées
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)   # on trie du plus grand au plus petit (pas sûr qu'on ait besoin, mais bon...)

    # Petite vérif (je pense que ça ne sert à rien mais au cas où)
    if n <= k:
        print(0)
        return
    res = 0
    # Ici je prends juste la somme en ignorant les K plus grands
    for idx in range(k, len(h)):
        res += h[idx]
    print(res)

if __name__ == "__main__":
    main()