liste = []
for i in range(100):
    liste.append(0)

liste[0] = 2
liste[1] = 1

i = 2
while i < 90:
    liste[i] = liste[i-1] + liste[i-2]
    i = i + 1

n = int(input())
print(liste[n])