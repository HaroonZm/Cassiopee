def read_input():
    return list(map(int, input().split()))

def read_n():
    return int(input())

def get_twoL_costs(q, h, s, d):
    return [q * 8, h * 4, s * 2, d]

def sort_list(l):
    l.sort()
    return l

def calc_even_cost(sorted_twoL, n):
    return sorted_twoL[0] * (n // 2)

def get_L_costs(q, h, s):
    return [q * 4, h * 2, s]

def calc_odd_cost(sorted_twoL, sorted_L, n):
    return sorted_twoL[0] * (n // 2) + sorted_L[0]

def main():
    q, h, s, d = read_input()
    n = read_n()
    twoL = get_twoL_costs(q, h, s, d)
    twoL = sort_list(twoL)
    if n % 2 == 0:
        ans = calc_even_cost(twoL, n)
    else:
        L = get_L_costs(q, h, s)
        L = sort_list(L)
        ans = calc_odd_cost(twoL, L, n)
    print(ans)

main()