table = [list(map(int, input().split())) for _ in range(10)]

def op(i, j):
    return table[i][j]

def check(ssn):
    val = 0
    for d in ssn:
        val = op(val, d)
    return val

bad_count = 0

for num in range(10000):
    digits = [num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10]
    e = 0
    for d in digits:
        e = op(e, d)
    ssn = digits + [e]

    detected = True

    # Check all single digit errors (alter one digit)
    for pos in range(5):
        original = ssn[pos]
        for new_digit in range(10):
            if new_digit == original:
                continue
            error_ssn = ssn[:]
            error_ssn[pos] = new_digit
            if check(error_ssn) == 0:
                detected = False
                break
        if not detected:
            break

    if not detected:
        bad_count += 1
        continue

    # Check all adjacent transposition errors
    for i in range(4):
        error_ssn = ssn[:]
        error_ssn[i], error_ssn[i+1] = error_ssn[i+1], error_ssn[i]
        if check(error_ssn) == 0:
            detected = False
            break

    if not detected:
        bad_count += 1

print(bad_count)