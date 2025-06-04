from sys import stdin

def compute_bill(w):
    thresholds = [10, 20, 30]
    rates = [125, 140, 160]
    bill = 1150
    prev = 0
    for th, rate in zip(thresholds, rates):
        if w > th:
            bill += (th - prev) * rate
            prev = th
        else:
            bill += (w - prev) * rate
            return 4280 - bill
    bill += (w - prev) * rates[-1]
    return 4280 - bill

for line in stdin:
    w = int(line)
    if w < 0:
        break
    print(compute_bill(w))