n = int(input())
total = 0
for x in range(n):
    total += int(input())

def moyenne(valeurs, count):
    return valeurs // count

print(moyenne(total, n))