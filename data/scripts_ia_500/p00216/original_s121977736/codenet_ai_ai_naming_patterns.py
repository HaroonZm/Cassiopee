while True:
    water_usage_liters = int(input())
    if water_usage_liters < 0:
        break
    base_cost_yen = 1150
    if water_usage_liters > 10:
        if water_usage_liters <= 20:
            base_cost_yen += (water_usage_liters - 10) * 125
        else:
            base_cost_yen += 1250
    if water_usage_liters > 20:
        if water_usage_liters <= 30:
            base_cost_yen += (water_usage_liters - 20) * 140
        else:
            base_cost_yen += 1400
    if water_usage_liters > 30:
        base_cost_yen += (water_usage_liters - 30) * 160
    total_bill_yen = 4280 - base_cost_yen
    print(total_bill_yen)