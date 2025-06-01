# AOJ 0159 The Best Body
# Python3 solution by me, with my quirks

TARGET_BMI = 22.0
TOLERANCE = 1e-5

while True:
    num_people = int(input())
    if num_people == 0:
        break
    best_id = 0
    smallest_diff = 1e9  # kinda arbitrary large number, could be better
    for _ in range(num_people):
        person_id, height_cm, weight_kg = map(int, input().split())
        bmi = weight_kg / ((height_cm / 100) ** 2)
        diff = abs(bmi - TARGET_BMI)
        # If difference is basically equal, pick the smaller ID
        if abs(diff - smallest_diff) < TOLERANCE:
            if person_id < best_id:
                best_id = person_id
        elif diff < smallest_diff:
            best_id = person_id
            smallest_diff = diff
    print(best_id)