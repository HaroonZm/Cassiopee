n = int(raw_input())  # nombre de toppings
a, b = map(float, raw_input().split(" "))
c = float(raw_input())

toppings = []
for _ in range(n):
    val = float(raw_input())
    toppings.append(val)

# Tri décroissant, manière un peu old-school avec cmp
toppings.sort(cmp=lambda x, y: cmp(y, x))

cal_sum = c
doll_sum = a

for i in range(n):
    # Je check si ça vaut le coup de rajouter ce topping
    if (cal_sum / doll_sum) < (cal_sum + toppings[i]) / (doll_sum + b):
        cal_sum += toppings[i]
        doll_sum += b
    else:
        break  # sinon on arrête direct

# Je retourne la partie entière de la moyenne
print int(cal_sum / doll_sum)