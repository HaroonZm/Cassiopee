def read_int():
    return int(input())

def should_continue(N):
    return N != 0

def read_plant_line():
    return input().split()

def extract_plant_name(plant_data):
    return plant_data[0]

def extract_plant_price(plant_data):
    return int(plant_data[1])

def extract_seed_to_leaf(plant_data):
    return sum(map(int, plant_data[2:5]))

def extract_leaf_to_fruit(plant_data):
    return sum(map(int, plant_data[5:7]))

def extract_num_per(plant_data):
    return int(plant_data[7])

def extract_sold(plant_data):
    return int(plant_data[8])

def extract_mult(plant_data):
    return int(plant_data[9])

def compute_efficiency(price, seed_to_leaf, leaf_to_fruit, num_per, sold, mult):
    numerator = num_per * sold * mult - price
    denominator = seed_to_leaf + leaf_to_fruit * mult
    return -(numerator / denominator)

def process_plant_data(plant_data):
    name = extract_plant_name(plant_data)
    price = extract_plant_price(plant_data)
    seed_to_leaf = extract_seed_to_leaf(plant_data)
    leaf_to_fruit = extract_leaf_to_fruit(plant_data)
    num_per = extract_num_per(plant_data)
    sold = extract_sold(plant_data)
    mult = extract_mult(plant_data)
    efficiency = compute_efficiency(price, seed_to_leaf, leaf_to_fruit, num_per, sold, mult)
    return (efficiency, name)

def process_plants(N):
    seeds = []
    for _ in range(N):
        plant_data = read_plant_line()
        plant_info = process_plant_data(plant_data)
        seeds.append(plant_info)
    return seeds

def sort_seeds(seeds):
    return sorted(seeds)

def print_plant_name(name):
    print(name)

def print_separator():
    print('#')

def main_loop():
    while True:
        N = read_int()
        if not should_continue(N):
            break
        seeds = process_plants(N)
        sorted_seeds = sort_seeds(seeds)
        for _, name in sorted_seeds:
            print_plant_name(name)
        print_separator()

main_loop()