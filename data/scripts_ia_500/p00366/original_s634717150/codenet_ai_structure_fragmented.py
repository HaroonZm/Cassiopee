def read_integer():
    return int(input())

def read_list_of_integers(n):
    result = []
    for _ in range(n):
        result.append(int(input()))
    return result

def sort_list(lst):
    lst.sort()

def max_of_list(lst):
    return lst[-1]

def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def increment_index_until(divisors, idx, value):
    while divisors[idx] < value:
        idx += 1
    return idx

def calculate_ans(n, values):
    if n == 1:
        return 0
    max_val = max_of_list(values)
    divisors = find_divisors(max_val)
    cur = 0
    ans = 0
    for t in values:
        cur = increment_index_until(divisors, cur, t)
        ans += divisors[cur] - t
    return ans

def main():
    N = read_integer()
    T = read_list_of_integers(N)
    sort_list(T)
    ans = calculate_ans(N, T)
    print(ans)

main()