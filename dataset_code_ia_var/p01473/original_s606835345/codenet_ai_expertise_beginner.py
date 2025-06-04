s = input()
count_dict = {}
for c in s:
    if c in count_dict:
        count_dict[c] += 1
    else:
        count_dict[c] = 1

odd_count = 0
for key in count_dict:
    if count_dict[key] % 2 != 0:
        odd_count += 1
        if odd_count > 1:
            print(0)
            break
        count_dict[key] -= 1
else:
    import math
    n = len(s) // 2
    result = math.factorial(n)
    for val in count_dict.values():
        result = result // math.factorial(val // 2)
    print(result)