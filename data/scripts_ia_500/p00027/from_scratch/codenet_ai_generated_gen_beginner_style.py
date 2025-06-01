days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# nombre de jours dans chaque mois de 2004 (année bissextile)
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    line = input()
    if line == "0 0":
        break
    m, d = map(int, line.split())
    total_days = 0
    # additionner les jours des mois précédents
    for i in range(m - 1):
        total_days += months[i]
    total_days += d
    # 1er Janvier 2004 est jeudi, qui est days[3]
    # on calcule l'indice du jour en faisant (total_days - 1 + 3) % 7
    index = (total_days - 1 + 3) % 7
    print(days[index])