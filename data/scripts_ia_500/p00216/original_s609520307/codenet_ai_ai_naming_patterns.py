import sys
import math
import os
import fractions

ENV_PYDEV = os.environ.get('PYDEV')
if ENV_PYDEV == "True":
    sys.stdin = open("sample-input.txt", "rt")

def calculate_water_bill(consumption_liters):
    BASE_CHARGE = 4280
    FIRST_TIER_MAX = 10
    SECOND_TIER_MAX = 20
    THIRD_TIER_MAX = 30

    FIRST_TIER_CHARGE = 1150
    SECOND_TIER_CHARGE = 1250
    THIRD_TIER_CHARGE = 1400

    FIRST_TIER_RATE = 1150
    SECOND_TIER_RATE = 125
    THIRD_TIER_RATE = 140
    FOURTH_TIER_RATE = 160

    if consumption_liters <= FIRST_TIER_MAX:
        return BASE_CHARGE - FIRST_TIER_RATE
    elif consumption_liters <= SECOND_TIER_MAX:
        return BASE_CHARGE - (FIRST_TIER_RATE + (consumption_liters - FIRST_TIER_MAX) * SECOND_TIER_RATE)
    elif consumption_liters <= THIRD_TIER_MAX:
        return BASE_CHARGE - (FIRST_TIER_RATE + SECOND_TIER_CHARGE + (consumption_liters - SECOND_TIER_MAX) * THIRD_TIER_RATE)
    else:
        return BASE_CHARGE - (FIRST_TIER_RATE + SECOND_TIER_CHARGE + THIRD_TIER_CHARGE + (consumption_liters - THIRD_TIER_MAX) * FOURTH_TIER_RATE)

while True:
    liters_consumed = int(input())
    if liters_consumed == -1:
        break
    print(calculate_water_bill(liters_consumed))