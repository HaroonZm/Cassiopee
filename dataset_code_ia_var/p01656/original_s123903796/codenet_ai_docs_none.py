N, Q = map(int, input().split())
rename = []
for i in range(N):
    year, name = input().split()
    year = int(year)
    rename.append([year, name])
if Q < rename[0][0]:
    print("kogakubu10gokan")
elif Q >= rename[-1][0]:
    print(rename[-1][1])
else:
    for i in range(N - 1):
        if rename[i][0] <= Q < rename[i + 1][0]:
            print(rename[i][1])