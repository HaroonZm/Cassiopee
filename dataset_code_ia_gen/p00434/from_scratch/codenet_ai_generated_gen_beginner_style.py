submitted = []
for i in range(28):
    num = int(input())
    submitted.append(num)

all_students = list(range(1, 31))

for num in all_students:
    if num not in submitted:
        print(num)