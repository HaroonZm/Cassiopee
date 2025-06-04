import sys

count_A = 0
count_B = 0
count_AB = 0
count_O = 0

for line in sys.stdin:
    line = line.strip()
    blood_type = line.split(',')[-1]
    if blood_type == 'A':
        count_A = count_A + 1
    elif blood_type == 'B':
        count_B = count_B + 1
    elif blood_type == 'AB':
        count_AB = count_AB + 1
    elif blood_type == 'O':
        count_O = count_O + 1

print(count_A)
print(count_B)
print(count_AB)
print(count_O)