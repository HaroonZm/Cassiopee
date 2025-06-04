n = int(input())
intervals = []
for _ in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))

max_lights = 0
for i in range(n):
    count = 0
    a_i, b_i = intervals[i]
    # On essaie avec la borne inférieure de l'intervalle i
    voltage = a_i
    for a, b in intervals:
        if a <= voltage <= b:
            count += 1
    if count > max_lights:
        max_lights = count

    count = 0
    # On essaie avec la borne supérieure de l'intervalle i
    voltage = b_i
    for a, b in intervals:
        if a <= voltage <= b:
            count += 1
    if count > max_lights:
        max_lights = count

print(max_lights)