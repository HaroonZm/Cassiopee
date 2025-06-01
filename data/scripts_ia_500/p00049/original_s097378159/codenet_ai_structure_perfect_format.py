l = ["A", "B", "AB", "O"]
dict = {"A": 0, "B": 0, "AB": 0, "O": 0}
while True:
    try:
        n, s = input().split(",")
    except:
        break
    dict[s] += 1
for i in l:
    print(dict[i])