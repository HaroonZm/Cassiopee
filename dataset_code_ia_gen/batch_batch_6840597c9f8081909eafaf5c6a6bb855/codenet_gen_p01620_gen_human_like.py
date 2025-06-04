def shift_station(c, shift):
    stations = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    idx = stations.index(c)
    new_idx = (idx - shift) % 52
    return stations[new_idx]

while True:
    n = int(input())
    if n == 0:
        break
    keys = list(map(int, input().split()))
    s = input()
    result = []
    for i, c in enumerate(s):
        shift = keys[i % n]
        result.append(shift_station(c, shift))
    print(''.join(result))