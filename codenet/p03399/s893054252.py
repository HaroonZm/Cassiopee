list = []
for i in range(4):
    list.append(int(input()))

train = [list[0], list[1]]
bus = [list[2], list[3]]

print(min(train)+min(bus))