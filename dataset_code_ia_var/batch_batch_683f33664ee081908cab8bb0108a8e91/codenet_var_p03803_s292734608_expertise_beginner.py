numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]

inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])

if numbers.index(a) > numbers.index(b):
    print("Alice")
elif numbers.index(a) == numbers.index(b):
    print("Draw")
else:
    print("Bob")