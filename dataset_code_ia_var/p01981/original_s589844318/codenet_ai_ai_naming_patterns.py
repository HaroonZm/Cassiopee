names_list = []
year_list = []
month_list = []
day_list = []
entry_count = -1

while True:
    try:
        input_values = input().split()
        names_list.append(input_values[0])
        year_list.append(int(input_values[1]))
        month_list.append(int(input_values[2]))
        day_list.append(int(input_values[3]))
        entry_count += 1
    except:
        break

for index in range(entry_count + 1):
    if year_list[index] > 31:
        names_list[index] = "?"
        year_list[index] -= 30
    elif year_list[index] == 31 and month_list[index] >= 5:
        names_list[index] = "?"
        year_list[index] -= 30

for index in range(entry_count + 1):
    print(f"{names_list[index]} {year_list[index]} {month_list[index]} {day_list[index]}")