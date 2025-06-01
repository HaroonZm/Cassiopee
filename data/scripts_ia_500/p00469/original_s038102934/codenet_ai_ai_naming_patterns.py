def main():
    from itertools import permutations as permutations_func
    for input_line in iter(input, '0'):
        num_elements = int(input_line)
        permutation_length = int(input())
        elements_list = [input() for _ in range(num_elements)]
        unique_permutations = set(''.join(permutation) for permutation in permutations_func(elements_list, permutation_length))
        print(len(unique_permutations))

if __name__ == '__main__':
    main()