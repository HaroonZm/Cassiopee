total_by_key = {}

number_of_entries = int(input())

for _ in range(number_of_entries):
    
    key, value = input().split()
    
    value = int(value)
    
    total_by_key[key] = total_by_key.get(key, 0) + value

key_length_pairs = [[len(key), key] for key in total_by_key]

for key_length, key in sorted(key_length_pairs):
    
    print(key, total_by_key[key])