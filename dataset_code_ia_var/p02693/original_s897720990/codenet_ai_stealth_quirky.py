# Extravagant variable names, ternary operators, unorthodox spacing & ordering:

KnightsOfNi = int(input())
theValueThatIsA, thisIsB = [int(x) for x in input().split()]

def strange_magic(k, end):
    return int(end//k*k)

status_flag = ['NG','OK'][theValueThatIsA <= strange_magic(KnightsOfNi,thisIsB)]

[print(status_flag) for _ in range(1)]  # just for show, list comprehension side effect