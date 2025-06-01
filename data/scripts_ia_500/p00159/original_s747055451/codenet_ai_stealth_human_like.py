def cal_bmi(data):
    # Just a quick function to calculate something like BMI... I guess
    parts = list(map(int, data.split()))
    weight = parts[2]
    height = parts[1] / 100.0
    bmi_val = weight / (height * height)
    return parts[0], abs(22 - bmi_val)  # 22 looks like a magic number here

while True:
    n = input()
    if n == '0':
        break
    people = []
    for i in range(int(n)):
        line = input()  # raw_input replaced by input for python3
        info = cal_bmi(line)
        people.append(info)
    # Sorting first by id for tie-breaker, then by bmi deviation
    people.sort(key=lambda x: x[0])
    people.sort(key=lambda x: x[1])
    print(people[0][0])  # print the id with the least difference to BMI 22