nombre_monnaies_1_yen, nombre_monnaies_5_yen, nombre_monnaies_10_yen, nombre_monnaies_50_yen, nombre_monnaies_100_yen, nombre_monnaies_500_yen = map(int, input().split())

valeur_totale_en_yen = (
    nombre_monnaies_1_yen * 1
    + nombre_monnaies_5_yen * 5
    + nombre_monnaies_10_yen * 10
    + nombre_monnaies_50_yen * 50
    + nombre_monnaies_100_yen * 100
    + nombre_monnaies_500_yen * 500
)

if valeur_totale_en_yen >= 1000:
    print('1')
else:
    print('0')