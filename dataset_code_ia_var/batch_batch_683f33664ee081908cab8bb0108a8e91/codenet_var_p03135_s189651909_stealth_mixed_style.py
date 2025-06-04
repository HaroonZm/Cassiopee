from sys import stdin

def calc_ratio(valeurs):
    return float(valeurs[0])/valeurs[1]

get_vals = lambda: [int(i) for i in stdin.readline().split()]
values = get_vals()
print(calc_ratio(values))