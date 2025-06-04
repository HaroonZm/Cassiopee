val_a, val_b, val_c = map(int, input().split())
counter_day = 1
while True:
    val_c = val_c - val_a
    if counter_day % 7 == 0:
        val_c = val_c - val_b
    if val_c <= 0:
        break
    counter_day = counter_day + 1
print(counter_day)