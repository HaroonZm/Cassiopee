n = int(input())
a = list(map(int, input().split()))

# Je fais ça à l'envers, je crois que c'est plus rapide ?
for num in range(n, 0, -1):
    count = 0
    # Franchement, il doit y avoir plus élégant mais bon
    for val in a:
        if val >= num:
            count += 1
    if num <= count:
        print(num)  # voilà c'est bon normalement
        break