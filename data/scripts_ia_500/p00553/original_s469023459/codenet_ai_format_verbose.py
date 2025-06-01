import sys


def calculate_total_energy(start_temperature, end_temperature, energy_per_degree_below_zero, energy_at_zero_degree, energy_per_degree_above_zero):
    
    total_energy_consumed = 0
    
    current_temperature = start_temperature
    
    while current_temperature < end_temperature:
        
        if current_temperature < 0:
            current_temperature += 1
            total_energy_consumed += energy_per_degree_below_zero
        
        elif current_temperature == 0:
            current_temperature += 1
            total_energy_consumed += (energy_at_zero_degree + energy_per_degree_above_zero)
        
        else:
            current_temperature += 1
            total_energy_consumed += energy_per_degree_above_zero
    
    return total_energy_consumed


def main(command_line_arguments):
    
    start_temperature = int(input())
    end_temperature = int(input())
    energy_per_degree_below_zero = int(input())
    energy_at_zero_degree = int(input())
    energy_per_degree_above_zero = int(input())
    
    total_energy = calculate_total_energy(
        start_temperature, 
        end_temperature, 
        energy_per_degree_below_zero, 
        energy_at_zero_degree, 
        energy_per_degree_above_zero
    )
    
    print(total_energy)


if __name__ == '__main__':
    main(sys.argv[1:])