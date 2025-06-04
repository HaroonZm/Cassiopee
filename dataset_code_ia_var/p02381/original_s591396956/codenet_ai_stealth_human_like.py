# Bon c'est parti, on va faire ce script... j'espère que ça va marcher!
import math

while True:
    n = int(input())
    if n == 0:
        # On sort si on a zéro, logique
        break
    values = input().split()
    numbers = []
    for v in values:
        numbers.append(int(v))
    sm = 0
    for nb in numbers:
        sm += nb
    moyenne = sm / n
    variance = 0
    i=0
    while i<n:
        val = (numbers[i] - moyenne) **2
        variance += val
        i=i+1
    variance = variance/n
    ecartType = math.sqrt(variance) # bon c'est sensé être ça
    print(ecartType)