temperature_values = []

for index in range(5):
    
    input_value = int(input())
    
    temperature_values.append(input_value)
    

total_cost = 0

initial_temperature = temperature_values[0]
cold_water_temperature = temperature_values[1]
heated_water_temperature = temperature_values[2]
fixed_heating_cost = temperature_values[3]
cost_per_cold_water_unit = temperature_values[4]

if initial_temperature < 0:
    
    temperature_increase = 0 - initial_temperature
    
    total_cost += temperature_increase * heated_water_temperature
    
    total_cost += fixed_heating_cost
    
    total_cost += cold_water_temperature * cost_per_cold_water_unit

elif initial_temperature > 0:
    
    temperature_difference = cold_water_temperature - initial_temperature
    
    total_cost += temperature_difference * cost_per_cold_water_unit

print(total_cost)