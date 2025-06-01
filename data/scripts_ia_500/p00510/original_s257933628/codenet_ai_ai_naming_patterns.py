nombre_clients = int(input())
montant_initial = int(input())
montant_maximum = montant_initial
consommations = []
for indice_client in range(nombre_clients):
    consommation_client = list(map(int, input().split()))
    consommations.append(consommation_client)
montant_courant = montant_initial
for consommation in consommations:
    montant_courant += consommation[0] - consommation[1]
    if montant_courant < 0:
        print(0)
        exit()
    montant_maximum = max(montant_courant, montant_maximum)
print(montant_maximum)