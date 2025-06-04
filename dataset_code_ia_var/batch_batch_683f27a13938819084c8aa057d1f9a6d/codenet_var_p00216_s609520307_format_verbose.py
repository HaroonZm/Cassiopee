import sys
import math
import os
import fractions

# Gérer le mode de développement si l'environnement le demande
python_development_mode = os.environ.get('PYDEV')
if python_development_mode == "True":
    sys.stdin = open("sample-input.txt", "rt")

def compute_monthly_water_bill(consumed_cubic_meters):
    """
    Calcule la facture d'eau corrigée selon une consommation mensuelle.
    """
    montant_de_base = 4280
    frais_pour_10m3 = 1150
    frais_pour_10m3_suivants = 1250
    frais_pour_10m3_apres_20 = 1400
    montant_par_m3_sup_10 = 125
    montant_par_m3_sup_20 = 140
    montant_par_m3_sup_30 = 160

    if consumed_cubic_meters <= 10:
        reduction_totale = frais_pour_10m3
    elif consumed_cubic_meters <= 20:
        reduction_totale = (
            frais_pour_10m3 +
            (consumed_cubic_meters - 10) * montant_par_m3_sup_10
        )
    elif consumed_cubic_meters <= 30:
        reduction_totale = (
            frais_pour_10m3 +
            frais_pour_10m3_suivants +
            (consumed_cubic_meters - 20) * montant_par_m3_sup_20
        )
    else:
        reduction_totale = (
            frais_pour_10m3 +
            frais_pour_10m3_suivants +
            frais_pour_10m3_apres_20 +
            (consumed_cubic_meters - 30) * montant_par_m3_sup_30
        )

    facture_finale = montant_de_base - reduction_totale
    return facture_finale

while True:

    cubic_meters_used_input = input()
    cubic_meters_used = int(cubic_meters_used_input)

    if cubic_meters_used == -1:
        break

    calculated_water_bill = compute_monthly_water_bill(cubic_meters_used)
    print(calculated_water_bill)