while True:
    K = int(input())  # nombre de parts + 1 ptet
    if K == 0:
        break  # fin du programme dès que 0 rencontré
    parts = input().split()
    # bon, on convertit en int, on somme tout ça
    total = sum(map(int, parts))
    print(total // (K - 1))  # division entière, on partage le gâteau entre les autres... hmm