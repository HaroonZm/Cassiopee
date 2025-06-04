def calculate_bmi(data_string):
    vals = data_string.split()
    height_cm = int(vals[1])
    weight = int(vals[2])
    # Here I'm calculating the bmi diff from 22, which is said to be ideal
    try:
        bmi_value = weight / ((height_cm/100.0)**2)
    except:
        bmi_value = 0 # just in case height is zero or so
    return (int(vals[0]), abs(22 - bmi_value))

while True:
    n = input()
    if n == 0:
        break
    people = []
    # Had to change because of Python3 input() stuff
    for j in range(int(n)):
        entry = input()
        people.append(calculate_bmi(entry))
    # Two sorts, maybe only one is needed? Meh, let's keep as is.
    best = sorted(sorted(people), key=lambda tup: tup[1])[0][0]
    print(best)