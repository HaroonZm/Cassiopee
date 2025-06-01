from collections import defaultdict

def main():
    def get_primes_upto(max_limit):
        is_prime_flags = [True] * (max_limit + 1)
        is_prime_flags[0] = False
        is_prime_flags[1] = False
        for current in range(2, int(max_limit ** 0.5) + 1):
            if is_prime_flags[current]:
                for multiple in range(current * current, max_limit + 1, current):
                    is_prime_flags[multiple] = False
        return [num for num in range(max_limit + 1) if is_prime_flags[num]]
    
    MAX_VALUE = 100000
    primes_list = get_primes_upto(MAX_VALUE)
    
    factors_by_number = [[] for _ in range(MAX_VALUE + 1)]
    for prime_num in primes_list:
        for multiple_num in range(prime_num, MAX_VALUE + 1, prime_num):
            factors_by_number[multiple_num].append(prime_num)
    
    input_length = int(input())
    input_values = list(map(int, input().split()))
    
    parent_representatives = [index for index in range(MAX_VALUE + 1)]
    
    def find_parent(element):
        if element == parent_representatives[element]:
            return element
        parent_representatives[element] = find_parent(parent_representatives[element])
        return parent_representatives[element]
    
    for index, value in enumerate(input_values):
        representative_primes = find_parent(min(factors_by_number[value]))
        for prime_factor in factors_by_number[value]:
            parent_representatives[find_parent(prime_factor)] = representative_primes
        parent_representatives[find_parent(value)] = representative_primes
    
    indices_by_representative = defaultdict(set)
    for index, value in enumerate(input_values):
        indices_by_representative[find_parent(value)].add(index)
    
    sorted_values = sorted(input_values)
    for index, value in enumerate(sorted_values):
        if index not in indices_by_representative[find_parent(value)]:
            print(0)
            break
    else:
        print(1)

main()