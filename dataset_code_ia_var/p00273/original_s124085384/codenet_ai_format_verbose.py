nombre_de_commandes = int(input())

for _ in range(nombre_de_commandes):

    prix_burger, prix_poutine, nombre_burgers, nombre_poutines = map(int, input().split())

    cout_total_sans_remise = (prix_burger * nombre_burgers) + (prix_poutine * nombre_poutines)

    if nombre_burgers < 5 and nombre_poutines < 2:

        cout_remise = ((prix_burger * 5) + (prix_poutine * 2)) * 0.8

        cout_final = min(cout_total_sans_remise, cout_remise)

    elif nombre_burgers >= 5 and nombre_poutines < 2:

        cout_remise = ((prix_burger * nombre_burgers) + (prix_poutine * 2)) * 0.8

        cout_final = min(cout_total_sans_remise, cout_remise)

    elif nombre_burgers < 5 and nombre_poutines >= 2:

        cout_remise = ((prix_burger * 5) + (prix_poutine * nombre_poutines)) * 0.8

        cout_final = min(cout_total_sans_remise, cout_remise)

    else:

        cout_final = cout_total_sans_remise * 0.8

    print(int(cout_final))