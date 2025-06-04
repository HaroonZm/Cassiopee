n = int(input())
numbers = input().split()
numbers = [int(x) for x in numbers]  # bon, on convertit tout en int ici

unique_numbers = set(numbers) # on met tout dans un set (oui c'est censé être plus rapide)
answer = len(unique_numbers) # combien ça en fait ?

print(answer) # voilà, c'est tout... normalement