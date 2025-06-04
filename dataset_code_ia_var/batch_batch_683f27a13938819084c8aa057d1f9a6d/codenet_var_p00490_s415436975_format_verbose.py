nombre_clients = int(input())

cout_fixe, cout_variable_par_client = map(int, input().split())

revenu_par_client = int(input())

list_revenus_clients = []

for _ in range(nombre_clients):
    saisie_revenu_client = int(input())
    list_revenus_clients.append(saisie_revenu_client)

revenus_tries_decroissants = sorted(list_revenus_clients, reverse=True)

meilleur_profit = 0

for nombre_clients_servis in range(1, nombre_clients):
    total_revenu = revenu_par_client + sum(revenus_tries_decroissants[:nombre_clients_servis])
    cout_total = cout_fixe + nombre_clients_servis * cout_variable_par_client
    profit_actuel = total_revenu // cout_total
    if profit_actuel > meilleur_profit:
        meilleur_profit = profit_actuel

print(meilleur_profit)