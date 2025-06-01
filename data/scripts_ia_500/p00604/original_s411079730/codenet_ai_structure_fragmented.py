def read_integer():
    try:
        return int(input())
    except:
        return None

def read_list_of_integers():
    return list(map(int, input().split()))

def sort_descending(lst):
    lst.sort(reverse=True)
    return lst

def compute_weighted_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += (i + 1) * lst[i]
    return total

def process():
    N = read_integer()
    if N is None:
        return None, None
    times = read_list_of_integers()
    return N, times

def main_loop():
    while True:
        N, times = process()
        if N is None:
            break
        times = sort_descending(times)
        ans = compute_weighted_sum(times)
        print(ans)

main_loop()