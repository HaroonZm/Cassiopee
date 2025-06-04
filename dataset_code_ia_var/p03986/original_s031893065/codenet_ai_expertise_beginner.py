s = input()

count_s = 0
result = 0

for letter in s:
    if letter == "S":
        count_s += 1
    else:
        if count_s > 0:
            count_s -= 1
        else:
            result += 1

result = result + count_s

print(result)