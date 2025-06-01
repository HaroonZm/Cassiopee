def read_number():
    return int(input())

def should_exit(n):
    return n == 0

def read_results(n):
    results = []
    for _ in range(n):
        results.append(input().split())
    return results

def count_zero(r):
    return r.count('0')

def count_one(r):
    return r.count('1')

def transform_result(r):
    name = r[0]
    zero_count = count_zero(r)
    one_count = count_one(r)
    return [name, zero_count, one_count]

def transform_results(results):
    transformed = []
    for r in results:
        transformed.append(transform_result(r))
    return transformed

def sort_results(results):
    results.sort(key=lambda x: (-x[1], x[2]))
    return results

def extract_names(results):
    names = []
    for r in results:
        names.append(r[0])
    return names

def print_results(results):
    print('\n'.join(results))

def main_loop():
    while True:
        n = read_number()
        if should_exit(n):
            break
        results = read_results(n)
        transformed = transform_results(results)
        sorted_results = sort_results(transformed)
        names = extract_names(sorted_results)
        print_results(names)

main_loop()