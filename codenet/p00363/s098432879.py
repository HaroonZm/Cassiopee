w, h, a = input().split()
w, h= int(w), int(h)
for i in range(h):
    if i in {0, h -1}:print("+" + "-" * (w - 2) + "+")
    else:print("|" + "." * ((w - 2) // 2) + a + "." * ((w - 2) // 2) + "|" if i == h // 2 else "|" + "." * (w - 2) + "|")