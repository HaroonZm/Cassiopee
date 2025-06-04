inn = input()
ans = "No"
try:
    if len(inn) >= 4:
        if inn[0] == "Y":
            if inn[1] == "A":
                if inn[2] == "K":
                    if inn[3] == "I":
                        ans = "Yes"
except:
    pass
print(ans)