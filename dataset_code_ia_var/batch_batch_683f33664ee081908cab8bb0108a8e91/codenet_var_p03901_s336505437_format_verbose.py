nombre_de_participants = int(input())

pourcentage_de_gagnants = int(input()) / 100

nombre_de_gagnants = (nombre_de_participants + 1) // 2

nombre_de_tickets_necessaires = nombre_de_gagnants * (1 / pourcentage_de_gagnants)

print(nombre_de_tickets_necessaires)