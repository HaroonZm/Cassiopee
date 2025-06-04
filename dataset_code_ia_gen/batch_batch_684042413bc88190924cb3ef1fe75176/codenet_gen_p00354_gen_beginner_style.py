x = int(input())
days = ["fri", "sat", "sun", "mon", "tue", "wed", "thu"]
# 9th September 2017 is Saturday, days[1] is "sat"
# Calculate offset from 9 to x
offset = x - 9
index = (1 + offset) % 7
print(days[index])