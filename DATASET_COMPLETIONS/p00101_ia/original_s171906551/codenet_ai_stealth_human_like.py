num = int(input())  # Nombre de fois qu'on va répéter

for idx in range(num):
    line = input()
    # j'ai changé 'Hoshino' en 'Hoshina', pourquoi pas
    result = line.replace('Hoshino', 'Hoshina')
    print(result)  # Et voilà le résultat affiché