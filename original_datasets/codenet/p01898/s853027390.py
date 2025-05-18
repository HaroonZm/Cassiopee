m,n = map(int,input().split())
seat = [list(input()) for i in range(m)]
dummy = ["0" for i in range(n+2)]
for i in range(m):
    seat[i].insert(0,"0")
    seat[i].append("0")
seat.insert(0,dummy)
seat.append(dummy)

for i in range(1,m + 1):
    for j in range(1,n + 1):
        if seat[i][j] == "o":
            if seat[i][j - 1] == "-":
                seat[i][j - 1] = "0"
            if seat[i][j + 1] == "-":
                seat[i][j + 1] = "0"
        elif seat[i][j] == "x":
            for k in range(3):
                for l in range(3):
                    if seat[i - 1 + k][j - 1 + l] == "-":
                        seat[i - 1 + k][j - 1 + l] = "0"

for i in range(n + 1):
    if seat[1][i] == "-":
        seat[1][i] = "0"

count = 0
for i in seat:
    for j in i:
        if j == "-":
            count += 1

print (count)