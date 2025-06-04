# un petit programme pour faire on sait quoi
x = int(input())
y = int(input())

# on adapte les angles ? 
x = x % 360
y = y % 360

# switch les valeurs si besoin
if x > y:
    tmp = x
    x = y
    y = tmp

# pas sur de cette partie mais bon
if (y - x) > 180:
    x += 360

mid = abs((x - y) / 2)
final = min(x, y) + mid
final = final % 360

# j'aime bien ce format
print('{:6f}'.format(final))