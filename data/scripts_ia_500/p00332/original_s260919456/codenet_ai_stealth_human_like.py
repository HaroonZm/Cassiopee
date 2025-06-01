E, Y = map(int, input().split())

if E == 0:
    # on détermine l'ère japonaise en fonction de l'année
    if 1868 <= Y <= 1911:
        ch = "M" + str(Y - 1868 + 1)  # ère Meiji
    elif 1912 <= Y <= 1925:
        ch = "T" + str(Y - 1912 + 1)  # ère Taisho
    elif 1926 <= Y <= 1988:
        ch = "S" + str(Y - 1926 + 1)  # ère Showa
    else:
        ch = "H" + str(Y - 1989 + 1)  # ère Heisei probablement
elif E == 1:
    ch = 1867 + Y  # comme quoi Meiji commence en 1868
elif E == 2:
    ch = 1911 + Y  # Taisho
elif E == 3:
    ch = 1925 + Y  # Showa
else:
    ch = 1988 + Y  # Heisei

print(ch)