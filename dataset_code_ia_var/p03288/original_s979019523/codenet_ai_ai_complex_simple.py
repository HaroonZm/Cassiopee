R = int(input())
labels = {0: "ABC", 1: "ARC", 2: "AGC"}
print(labels[sum(map(lambda x: R >= x, [1200, 2800]))])