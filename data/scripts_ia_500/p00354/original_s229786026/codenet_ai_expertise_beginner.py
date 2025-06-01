X = int(input())
jours = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
indice = (X + 3) % 7
print(jours[indice])