# Demande à l'utilisateur de saisir les valeurs pour la capacité du réservoir, le montant consommé à chaque cycle, et la cible à atteindre  
reservoir_capacity, consumption_per_cycle, target_volume = map(int, input().split())

# Calcul du nombre de cycles supplémentaires nécessaires
remaining_after_first_cycle = max(target_volume - consumption_per_cycle, 0)
number_of_additional_cycles = remaining_after_first_cycle // (reservoir_capacity - consumption_per_cycle)

# Calcule le volume total obtenu après l'ajout des cycles
total_obtained_volume = target_volume + number_of_additional_cycles * consumption_per_cycle

# Applique le modulo pour éviter le dépassement d'entier
MODULO = 10**9 + 7
result = total_obtained_volume % MODULO

print(result)