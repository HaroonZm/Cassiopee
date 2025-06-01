x = int(input())
jours = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
index = (x + 3) % 7
print(jours[index])