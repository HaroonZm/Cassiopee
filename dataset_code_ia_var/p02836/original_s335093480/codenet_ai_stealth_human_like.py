# ok, on lit l'entrée utilisateur
ch = input()
total = 0

# je pense qu'on peut faire ça comme ça ?
for idx in range(int(len(ch)/2)):
    if ch[idx] != ch[len(ch)-1-idx]:
        total = total + 1   # incrémentation (ça marche ?)
# le résultat c'est ce qu'on voulait
print(total)