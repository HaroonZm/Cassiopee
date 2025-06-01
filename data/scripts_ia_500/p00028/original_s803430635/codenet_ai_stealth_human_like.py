counts = {}
max_count = 1
while True:
    try:
        num = int(input())
        if num in counts:
            counts[num] += 1
            if counts[num] > max_count:
                max_count = counts[num]  # Update the max count if needed
        else:
            counts[num] = 1
    except:
        # Probably reached EOF or invalid input, so stop reading
        break

sorted_items = sorted(counts.items())  # Sort by the keys
for number, freq in sorted_items:
    if freq == max_count:
        print(number)  # Print numbers with the highest occurrence