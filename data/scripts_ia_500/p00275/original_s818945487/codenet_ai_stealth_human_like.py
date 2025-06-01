def play(line, N):
    counts = [0 for _ in range(N)]
    bonus = 0

    for idx in range(len(line)):
        pos = idx % N
        char = line[idx]

        if char == 'M':
            counts[pos] += 1
        elif char == 'S':
            counts[pos] += 1
            bonus += counts[pos]
            counts[pos] = 0
        elif char == 'L':
            counts[pos] += bonus + 1
            bonus = 0
        # no other chars expected, ignoring them

    counts.sort()  # sort to get them in order, I guess?

    for val in counts:
        print(val, end=' ')
    print(bonus)  # print the leftover bonus too

while True:
    N = int(input())
    if N == 0:
        break
    line = input()
    play(line, N)