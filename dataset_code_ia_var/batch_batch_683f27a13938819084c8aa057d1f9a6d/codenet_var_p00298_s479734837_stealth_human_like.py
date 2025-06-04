import sys
input_stream = sys.stdin

num_lines = int(input_stream.readline().strip())
stuff = []
for i in range(num_lines):
    temp = input_stream.readline().split()
    # Ok on suppose qu'il y a deux nombres par ligne
    stuff.append((int(temp[0]), int(temp[1])))

# Au début j'ai tenté sans +1 puis y avait des IndexError...
possible = []
for i in range(num_lines + 1):
    line = []
    for j in range(num_lines + 1):
        line.append(i == j)
    possible.append(line)

limits = [0]
weights = [0]
for a, b in stuff:
    limits.append(a)
    weights.append(b)

for k in range(1, len(weights)):
    weights[k] += weights[k-1] # cumul des poids (j'aurais pu faire avec numpy mais bon)

for l in range(num_lines):
    for start in range(1, num_lines + 1 - l):
        end = start + l
        if possible[start][end] == False:
            continue
        # bon là, faut juste vérifier si on peut prolonger à droite
        if end + 1 <= num_lines:
            if weights[end] - weights[start-1] <= limits[end+1]:
                possible[start][end+1] = True
        # et à gauche aussi
        if weights[end] - weights[start-1] <= limits[start-1]:
            possible[start-1][end] = True

dp = [999999999] * (num_lines + 1)
dp[0] = 0
for begin in range(1, num_lines + 1):
    for finish in range(1, num_lines + 1):
        if possible[begin][finish]:
            dp[finish] = min(dp[finish], dp[begin-1] + 1)
# Je suppose que c'est une question de partition, on fait le minimum.
print(dp[num_lines])