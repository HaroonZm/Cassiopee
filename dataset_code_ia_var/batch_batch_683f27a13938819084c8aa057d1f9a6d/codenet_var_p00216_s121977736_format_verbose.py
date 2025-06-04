while True:

    water_usage_in_cubic_meters = int(input())

    if water_usage_in_cubic_meters < 0:
        break

    total_water_bill_in_yen = 1150

    if water_usage_in_cubic_meters > 10:
        if water_usage_in_cubic_meters <= 20:
            total_water_bill_in_yen += (water_usage_in_cubic_meters - 10) * 125
        else:
            total_water_bill_in_yen += 10 * 125

    if water_usage_in_cubic_meters > 20:
        if water_usage_in_cubic_meters <= 30:
            total_water_bill_in_yen += (water_usage_in_cubic_meters - 20) * 140
        else:
            total_water_bill_in_yen += 10 * 140

    if water_usage_in_cubic_meters > 30:
        total_water_bill_in_yen += (water_usage_in_cubic_meters - 30) * 160

    water_bill_savings_in_yen = 4280 - total_water_bill_in_yen

    print(water_bill_savings_in_yen)