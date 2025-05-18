n = int(input())
series = [int(x) for x in input().split()]

odd_dict = {}
even_dict = {}

for i in range(n):
    k = series[i]
    if i % 2 == 0:
        try:
            even_dict[k] += 1
        except KeyError:
            even_dict[k] = 1 
    else:
        try:
            odd_dict[k] += 1
        except KeyError:
            odd_dict[k] = 1

odd_vals = []
even_vals = []

for key in odd_dict.keys():
    odd_vals.append([odd_dict[key], key])
for key in even_dict.keys():
    even_vals.append([even_dict[key], key])

odd_vals.sort(reverse=True)
even_vals.sort(reverse=True)

# print(odd_vals)
# print(even_vals)

if len(odd_vals) == 1 and len(even_vals) == 1:
    a = odd_vals[0][0]
    b = even_vals[0][0]

    if odd_vals[0][1] != even_vals[0][1]:
        print(n - a - b)
    else:
        print(n // 2)
elif len(odd_vals) > 1 and len(even_vals) > 1:
    if odd_vals[0][1] != even_vals[0][1]:
        print(n - odd_vals[0][0] - even_vals[0][0])
    else:
        a = odd_vals[0][0]
        b = odd_vals[1][0]
        c = even_vals[0][0]
        d = even_vals[1][0]
        print(min(n - a - d, n - b - c))
else:
    a = odd_vals[0][0]
    b = even_vals[0][0]
    c = 0
    if len(odd_vals) == 1:
        c = even_vals[1][0]
    else:
        c = odd_vals[1][0]
    
    if odd_vals[0][1] != even_vals[0][1]:
        print(n - a - b)
    else:
        print(n - a - c)

# print(even_dict)
# print(odd_dict)