import bisect

# Lecture du nombre de paquets et du nombre de clients
number_of_parcels, number_of_clients = map(int, input().split())

# Lecture des poids et temps des paquets
parcels_data = [tuple(map(int, input().split())) for _ in range(number_of_parcels)]
parcel_weights, parcel_times = map(list, zip(*parcels_data))

# Calcul des sommes cumulées de poids et de temps pour les paquets
for parcel_index in range(1, number_of_parcels):
    parcel_weights[parcel_index] += parcel_weights[parcel_index - 1]
    parcel_times[parcel_index] += parcel_times[parcel_index - 1]

# Lecture des contraintes de poids et de temps pour les clients
clients_data = [tuple(map(int, input().split())) for _ in range(number_of_clients)]
client_weight_limits, client_time_limits = map(list, zip(*clients_data))

# Dictionnaire pour stocker l'état de la répartition des colis restants (clés: indices restants, valeurs: dernier colis attribué)
remaining_parcels_state = {}
remaining_parcels_state[tuple(range(number_of_clients))] = -1

# Boucle sur le nombre de clients
for iteration in range(number_of_clients):

    current_state_items = [(key, remaining_parcels_state[key]) for key in remaining_parcels_state]
    next_state = {}

    for state_entry in current_state_items:
        client_indices_tuple, last_parcel_index_used = state_entry

        for client_position in client_indices_tuple:
            if last_parcel_index_used != -1:
                # Chercher l'indice max du colis pouvant satisfaire le client à partir du dernier colis attribué
                max_weight_index = bisect.bisect_right(parcel_weights, client_weight_limits[client_position] + parcel_weights[last_parcel_index_used], last_parcel_index_used)
                max_time_index = bisect.bisect_right(parcel_times, client_time_limits[client_position] + parcel_times[last_parcel_index_used], last_parcel_index_used)
                assignable_parcel_index = min(max_weight_index, max_time_index) - 1
            else:
                # Premier client, comparer avec zéro comme base
                max_weight_index = bisect.bisect_right(parcel_weights, client_weight_limits[client_position])
                max_time_index = bisect.bisect_right(parcel_times, client_time_limits[client_position])
                assignable_parcel_index = min(max_weight_index, max_time_index) - 1

            # Générer le nouvel état sans ce client
            remaining_clients_indices = list(client_indices_tuple)
            remaining_clients_indices.remove(client_position)
            remaining_clients_tuple = tuple(remaining_clients_indices)

            # Mettre à jour le meilleur index de colis atteignable dans l'état suivant
            if remaining_clients_tuple in next_state:
                next_state[remaining_clients_tuple] = max(next_state[remaining_clients_tuple], assignable_parcel_index)
            else:
                next_state[remaining_clients_tuple] = assignable_parcel_index

    remaining_parcels_state = next_state

# Calcul du résultat final : nombre maximum de colis pouvant être attribués
print(max([remaining_parcels_state[state_key] for state_key in remaining_parcels_state]) + 1)