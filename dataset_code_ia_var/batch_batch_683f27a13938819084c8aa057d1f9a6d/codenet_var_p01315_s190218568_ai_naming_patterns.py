while True:
    num_plants = int(input())
    if num_plants == 0:
        break
    plant_entries = []
    for plant_idx in range(num_plants):
        plant_data = input().split()
        plant_name = plant_data[0]
        plant_price = int(plant_data[1])
        plant_seed_to_leaf = sum(map(int, plant_data[2:5]))
        plant_leaf_to_fruit = sum(map(int, plant_data[5:7]))
        plant_num_per = int(plant_data[7])
        plant_sold = int(plant_data[8])
        plant_multiplier = int(plant_data[9])
        plant_score = -(
            (plant_num_per * plant_sold * plant_multiplier - plant_price)
            / (plant_seed_to_leaf + plant_leaf_to_fruit * plant_multiplier)
        )
        plant_entries.append((plant_score, plant_name))
    for _, output_plant_name in sorted(plant_entries):
        print(output_plant_name)
    print('#')