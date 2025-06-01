C = list()
i = 0
while i < 5:
    X = int(input())
    if X < 40:
        X = 40
    C += [X]
    i += 1

def average(lst):
    return sum(lst) // len(lst)

print(average(C))