l = ["A", "B", "AB", "O"]
d = {"A":0, "B":0, "AB":0, "O":0}

while True:
    ligne = input()
    if ligne == "":
        break
    try:
        n_s = ligne.split(",")
        n = n_s[0]
        s = n_s[1]
        d[s] = d[s] + 1
    except:
        break

for i in l:
    print(d[i])