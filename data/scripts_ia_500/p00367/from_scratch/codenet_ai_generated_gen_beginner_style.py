N = int(input())

customers = []

for _ in range(N):
    data = list(map(int, input().split()))
    # breakfast start
    ast = data[0]*60 + data[1]
    aet = data[2]*60 + data[3]
    hst = data[4]*60 + data[5]
    het = data[6]*60 + data[7]
    bst = data[8]*60 + data[9]
    bet = data[10]*60 + data[11]
    customers.append(((ast,aet),(hst,het),(bst,bet)))

max_count = 0

# try all possible times for breakfast, lunch, supper from 0 to 1439 minutes
for btime in range(0, 1440):
    for ltime in range(btime+1, 1440):
        for stime in range(ltime+1, 1440):
            count = 0
            for c in customers:
                breakfast = c[0]
                lunch = c[1]
                supper = c[2]

                if breakfast[0] <= btime <= breakfast[1] and lunch[0] <= ltime <= lunch[1] and supper[0] <= stime <= supper[1]:
                    count += 1

            if count > max_count:
                max_count = count

print(max_count)