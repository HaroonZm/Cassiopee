X = int(input())
days = ["fri", "sat", "sun", "mon", "tue", "wed", "thu"]
# 9th September 2017 is Saturday, index 1
index = (X - 1 + 5) % 7
print(days[index])