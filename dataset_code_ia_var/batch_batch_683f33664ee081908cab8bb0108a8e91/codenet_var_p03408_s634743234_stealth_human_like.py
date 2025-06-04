import collections

# on va récupérer les entrées
num = int(input())  # combien ? pourquoi pas N
lst1 = []
for _ in range(num):
    lst1.append(input().strip())

num2 = int(input())
lst2 = []
for _ in range(num2):
    lst2.append(input())  # je suppose que .strip() n'est pas indispensable

counter1 = collections.Counter(lst1)
counter2 = collections.Counter(lst2)

# Bon, calcule la différence max, si j'ai bien compris
max_val = 0
for k in counter1:
    tmp = counter1[k] - counter2.get(k, 0)
    if tmp > max_val:
        max_val = tmp

print(max_val if max_val > 0 else 0)  # bon, c'est plus clair pour moi comme ça...