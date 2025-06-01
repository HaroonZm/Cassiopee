X = int(input())

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# 9th September 2017 is Saturday, which is index 5 in days (starting from 0)
index_9 = 5

# Calculate difference from 9
diff = X - 9

# Calculate the day index
day_index = (index_9 + diff) % 7

print(days[day_index])