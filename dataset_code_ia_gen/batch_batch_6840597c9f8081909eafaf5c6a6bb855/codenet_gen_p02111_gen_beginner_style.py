theta = int(input())

# Chaque heure correspond à 30 degrés (360° / 12 heures)
# Chaque minute correspond à 0.5 degrés (30° / 60 minutes)
total_minutes = int(theta / 0.5)

h = total_minutes // 60
m = total_minutes % 60

print(h, m)