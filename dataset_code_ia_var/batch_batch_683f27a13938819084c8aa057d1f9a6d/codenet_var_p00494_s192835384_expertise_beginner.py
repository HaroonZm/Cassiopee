import re

s = input()
pattern = "(J*)(O*)(I*)"
result = re.findall(pattern, s)

max_o = 0

for tup in result:
    count_j = len(tup[0])
    count_o = len(tup[1])
    count_i = len(tup[2])
    if count_j >= count_o and count_i >= count_o:
        if count_o > max_o:
            max_o = count_o

print(max_o)