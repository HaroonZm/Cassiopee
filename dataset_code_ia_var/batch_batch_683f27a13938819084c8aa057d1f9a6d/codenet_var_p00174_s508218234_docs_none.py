from collections import Counter

while True:
    input_item = input()
    if input_item == "0":
        break
    input_list = [input_item, input(), input()]
    for item in input_list:
        count = Counter(item)
        count[item[0]] -= 1
        if count["A"] > count["B"]:
            count["A"] += 1
        else:
            count["B"] += 1
        print(count["A"], count["B"])