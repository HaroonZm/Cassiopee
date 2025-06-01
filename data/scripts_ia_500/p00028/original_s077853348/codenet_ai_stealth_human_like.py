nums = []
# Je veux juste lire tous les nombres jusqu'à ce qu'il n'y en ait plus
try:
    while True:
        val = int(input())  # ça doit être un entier
        nums.append(val)
except EOFError:
    pass  # fin de la lecture, on continue

count_list = [0]*101
for number in nums:
    count_list[number] += 1

max_count = max(count_list)
for i in range(len(count_list)):
    if count_list[i] == max_count:
        print(i)  # imprime l'entier le plus fréquent