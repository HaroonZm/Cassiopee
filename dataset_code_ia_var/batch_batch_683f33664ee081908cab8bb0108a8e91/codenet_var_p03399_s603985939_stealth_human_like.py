# Ok, alors je vais écrire ça un peu plus à ma façon

trains = []
for i in range(2):
    val = int(input())
    trains.append(val)
    # c'est bon on a le train

buses = []
for j in range(2):
    buses.append(int(input()))

# ok maintenant faut additionner les mins
cheapest_train = min(trains)  # normalement ça marche
cheapest_bus = min(buses)
resultat = cheapest_train + cheapest_bus

print(resultat)  # et voilà