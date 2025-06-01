my_list = []

for x in range(6):
    val = int(input())
    my_list.append(val)

first_part = my_list[:4]
second_part = my_list[4:]

first_part.sort()
# removing the smallest number from first part
del first_part[0]

second_part.sort()
del second_part[0]  # also getting rid of the smallest here

total = sum(first_part) + sum(second_part)

print(total)