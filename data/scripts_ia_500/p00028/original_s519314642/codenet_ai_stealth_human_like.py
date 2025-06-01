numbers = []
try:
    while True:
        # je prends les nombres un par un
        num = int(input())
        numbers.append(num)
except EOFError:
    # fin de la lecture des données, on continue
    pass

freq = [0] * 101  # fréquence des nombres de 0 à 100

for number in numbers:
    freq[number] += 1

max_count = max(freq)
# bah oui, on imprime tous ceux qui ont la fréquence max
for i in range(len(freq)):
    if freq[i] == max_count:
        print(i)