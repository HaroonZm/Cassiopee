i = 0
j = 0
k = 0
l = 0

while True:
    sides = input().split()
    sides = [int(x) for x in sides]
    
    if min(sides) <= 0:
        break
    
    total = sum(sides)
    longest = max(sides)
    if total - longest <= longest:
        break
    
    i += 1
    
    max_index = sides.index(longest)
    
    sum_squares = 0
    for x in sides:
        sum_squares += x * x
    
    cos_numerator = sum_squares - 2 * (longest ** 2)
    cos_denominator = 2 * total - 2 * longest
    
    cos_value = cos_numerator / cos_denominator
    
    if cos_value < 0:
        l += 1
    elif cos_value > 0:
        k += 1
    else:
        j += 1

print(i, j, k, l)