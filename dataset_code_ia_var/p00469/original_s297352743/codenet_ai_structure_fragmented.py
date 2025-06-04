import itertools

def read_int():
    return int(input())

def read_input_pair():
    n = read_int()
    k = read_int()
    return n, k

def is_end_of_input(n, k):
    return (n, k) == (0, 0)

def read_string():
    return input()

def read_strings(n):
    strings = []
    for _ in range(n):
        strings.append(read_string())
    return strings

def get_permutations(elements, k):
    return list(itertools.permutations(elements, k))

def join_tuple_elements(tpl):
    return "".join(tpl)

def generate_words_from_permutations(permutations):
    words = []
    for item in permutations:
        word = join_tuple_elements(item)
        words.append(word)
    return words

def count_unique_words(words):
    unique_words = set(words)
    return len(unique_words)

def main_loop():
    while True:
        n, k = read_input_pair()
        if is_end_of_input(n, k):
            break
        num_lis = read_strings(n)
        permutations = get_permutations(num_lis, k)
        word_list = generate_words_from_permutations(permutations)
        unique_count = count_unique_words(word_list)
        print(unique_count)

def main():
    main_loop()

main()