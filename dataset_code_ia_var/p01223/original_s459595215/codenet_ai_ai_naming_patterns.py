nb_cases = int(input())
while nb_cases:
    input()
    nb_cases -= 1
    arr_values = list(map(int, input().split()))
    max_increase = 0
    max_decrease = 0
    for idx in range(1, len(arr_values)):
        diff = arr_values[idx] - arr_values[idx - 1]
        if diff > 0:
            max_increase = max(diff, max_increase)
        elif diff < 0:
            max_decrease = max(-diff, max_decrease)
    print(max_increase, max_decrease)