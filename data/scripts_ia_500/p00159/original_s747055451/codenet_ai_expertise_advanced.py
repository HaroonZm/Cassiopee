def bmi(data):
    w, h, a = map(int, data.split())
    bmi_val = a / (h / 100) ** 2
    return w, abs(22 - bmi_val)

while True:
    n = input()
    if n == '0':
        break
    entries = [bmi(input()) for _ in range(int(n))]
    print(min(entries, key=lambda x: x[1])[0])